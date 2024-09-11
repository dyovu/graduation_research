import socket
import threading
import os

from mcp_receiver.process_packet import process_packet


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
        self.process_packet = process_packet
    
    def start(self, queue):
        print("run")
        self.queue = queue
        self.thread = threading.Thread(target=self.loop, args=())
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
        
    def loop(self):
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
                # print(message)

                #messageをdeserializeする
                #使うデータによって変える
                data = self.process_packet(message)
                self.queue.put(data)
                # print(data)
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
