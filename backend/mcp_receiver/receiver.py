import socket
import threading
import asyncio 
import os
import time


from backend.mcp_receiver.process_packet import process_packet
from backend.mcp_receiver.convert_tran_data import convert_tran_data
from backend.mcp_receiver.convert_tran_data_pq import convert_tran_data_pq
from backend.manager.choreography_manager import ChoreographyManager, get_choreography_manager
from backend.service.insert_real_time_data import insert_real_time_data
from backend.service.insert_correct_manager import insert_correct_manager
from backend.service.compare import compare
# from backend.service.check_sim import check_sim


class Receiver():
    #ipaddrは 192.168~ を記述する
    #dockerコンテナ内で実行する場合はループバックアドレスor0.0.0.0
    #dockerコンテナ外のport番号を記述する
    roopback = "127.0.0.1"
    roopback2 = "0.0.0.0"
    def __init__(self, addr = roopback2, port = 12351):
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
        self.choreography_manager:ChoreographyManager = get_choreography_manager()
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
    

    def loop(self,use_insert_right_arm):
        print("loop")
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((self.addr, self.port))
        self.socket.settimeout(1.0)
        # range_of_motion = {"x_min": [], "y_min": [], "z_min": [], "x_max": [], "y_max": [], "z_max": []}
        previous = {}

        while self.running:
            try:
                message, client_addr = self.socket.recvfrom(2048)
                data = process_packet(message)

                converted_data = convert_tran_data(data, previous)
                # converted_data = convert_tran_data_pq(data, previous)

                # print("data", data)
                # print("converted_data", converted_data)
                
                if use_insert_right_arm:
                    """
                        比較する際にのみ使用する関数はこのif分の中に記述する
                    """
                    if not previous == {} and converted_data != None:
                        insert_real_time_data(previous)
                        compare(self.choreography_manager)
                

                # skdfでNoneが帰ってくる可能性がある
                if converted_data != None:
                    previous = converted_data
                
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

        # print(range_of_motion)

        # whileと同じ位置
        if self.socket:
            self.socket.close()
