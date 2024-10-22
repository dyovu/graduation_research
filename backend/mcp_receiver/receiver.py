import socket
import threading
import asyncio 
import os
import time

from scipy.spatial.distance import cosine

from backend.mcp_receiver.process_packet import process_packet
from backend.mcp_receiver.convert_tran_data import convert_tran_data
from backend.manager.db_data_manager import DbDataManager, get_db_data_manager
from backend.service.insert_real_time_data import insert_real_time_data
from backend.service.compare import compare
from backend.service.check_sim import check_sim
from backend.service.show_quaternion import show_quaternion


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

    # insert用データ取得開始ボタン
    def start_insert(self, queue):
        print("get_insert_data")
        self.queue = queue
        self.thread = threading.Thread(target=self.loop, args=(False,))
        self.running = True
        self.thread.start()
    
    # compare用データ取得開始ボタン
    def start_compare(self, queue):
        print("get_compare_data")
        self.queue = queue
        self.db_data_manager:DbDataManager = get_db_data_manager()
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
        range_of_motion = {"x_min": [], "y_min": [], "z_min": [], "x_max": [], "y_max": [], "z_max": []}

        while self.running:
            try:
                print('----------------------')
                #mocopiからバイナリーデータ送られてくるのを受け取る
                message, client_addr = self.socket.recvfrom(2048)
                data = process_packet(message)
                converted_data = convert_tran_data(data, range_of_motion)
                # print("data", data)
                print("converted_data", converted_data)
                
                
                if use_insert_right_arm:
                    # ---------------------------------
                    # 比較する際にのみ使用する関数はこのif分の中に記述する
                    # ---------------------------------
                    insert_real_time_data(data, converted_data)
                    compare(self.db_data_manager, self.lock)
                    pass
                else:
                    # ---------------------------------
                    # insert_startでloopしている時だけ呼び出す
                    # ---------------------------------
                    insert_real_time_data(data, converted_data)
                    # show_quaternion(data)
                    # check_sim()
                    pass

                self.queue.put(converted_data)
                
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

        print(range_of_motion)

        # whileと同じ位置
        if self.socket:
            self.socket.close()
