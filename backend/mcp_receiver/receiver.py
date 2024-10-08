import socket
import threading
import asyncio 
import os
import time

from backend.mcp_receiver.process_packet import process_packet
from backend.service.store_user_data import insert_real_time_data
from backend.service.compare import compare
from backend.service.check_cos import check_cos
from backend.manager.db_data_manager import DbDataManager, get_db_data_manager


class Receiver():
    #ipaddrは 192.168~ を記述する
    #dockerコンテナ内で実行する場合はループバックアドレスor0.0.0.0
    #dockerコンテナ外のport番号を記述する
    roopback = "127.0.0.1"
    roopback2 = "0.0.0.0"
    def __init__(self, addr = roopback2, port = 12351):
        self.lock = threading.Lock()
        self.addr = addr
        self.port = port
        self.running = False
        self.socket = None
        self.process_packet = process_packet

    # insert用データ取得開始ボタン
    def start_insert(self, queue, compare_manager):
        print("get_insert_data")
        self.queue = queue
        self.compare_manager = compare_manager
        self.thread = threading.Thread(target=self.loop, args=(False,))
        self.running = True
        self.thread.start()
    
    # compare用データ取得開始ボタン
    def start_compare(self, queue, compare_manager):
        print("get_compare_data")
        self.queue = queue
        self.db_data_manager:DbDataManager = get_db_data_manager()
        self.compare_manager = compare_manager
        self.thread = threading.Thread(target=self.loop, args=(True,))
        self.running = True
        self.thread.start()

    def stop(self):
        print("stop")
        self.running = False  # スレッドを停止中に設定
        if self.socket:
            self.socket.close()  # ソケットを閉じる
        if self.thread:
            self.thread.join() #スレッドの停止を待つ
        #ここでqueueからデータを取り出してデータベースに挿入するプログラムを書く（現在はweb上に表示する)
    

    # inset, compareそれぞれに対応するloopを作る
    def loop(self,use_insert_right_arm):
        print('loop')
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((self.addr, self.port))
        #データが送られてこない時にずっと待受をしているのを防ぐ
        self.socket.settimeout(1.0)

        while self.running:
            try:
                print('----------------------------------')
                #mocopiからバイナリーデータ送られてくるのを受け取る
                message, client_addr = self.socket.recvfrom(2048)
                data = self.process_packet(message)
                # print(data)

                # ---------------------------------
                # 比較する際にのみ使用する関数はこのif分の中に記述する
                # ---------------------------------
                if use_insert_right_arm:
                    # print("use_insert_right_arm is True")
                    insert_real_time_data(data, self.compare_manager)
                    compare(self.compare_manager, self.db_data_manager)
                    print("current_index is ", self.compare_manager.current_index)
                    
                    if self.compare_manager.current_index >= 5000:
                        with self.lock:
                            self.running = False
                        break
                else:
                    insert_real_time_data(data, self.compare_manager)
                    check_cos()
                    # print(data)
                self.queue.put(data)
                
            except socket.timeout:
                continue
            except socket.error as e:
                if not self.running:
                    # ソケットが閉じられているときの例外は無視する
                    break
                else:
                    print(e)
            except KeyError as e:
                print(e)

        # whileと同じ位置
        if self.socket:
            self.socket.close()
