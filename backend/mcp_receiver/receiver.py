import socket
import threading
import os
import time

from backend.mcp_receiver.process_packet import process_packet
from backend.service.store_user_data import insert_right_arm
from backend.service.compare import compare


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

    # 2つの開始メソッドをinsert用とcompare用に変更する
    def start_insert(self, queue):
        print("run")
        self.queue = queue
        self.thread = threading.Thread(target=self.loop, args=(False,))
        self.running = True
        self.thread.start()
    
    # ここのループを変える
    def start_compare(self, queue, compare_manager, db_data_manager):
        print("run")
        self.queue = queue
        self.compare_manager = compare_manager
        self.db_data_manager = db_data_manager
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

                # ---------------------------------
                # 比較する際にのみ使用する関数はこのif分の中に記述する
                # ---------------------------------
                if use_insert_right_arm:
                    insert_right_arm(data, self.compare_manager)
                    if self.compare_manager.current_index%5 == 0 and  (self.compare_manager.current_index > self.db_data_manager.right_arm_frame):
                        compare(self.compare_manager)
                    # print(self.receiver_manager.right_arm)

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
