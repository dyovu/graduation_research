# receiver_manager.py

import queue
import numpy as np

"""""
このクラスはシングルトンパターン（クラスのインスタンスが1つだけ存在することを保証する）
"""""

class CompareManager:
    # クラス変数 : クラス内で普遍の変数。いくつインスタンスを作ってもこの値は変わらない。
    _instance = None
    _max_frame = 3600

    # _instanceが存在するかどうか
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CompareManager, cls).__new__(cls)
            # 遅延インポート
            from backend.mcp_receiver.receiver import Receiver
            cls._instance.receiver = Receiver()
            cls._instance.data_queue = queue.Queue()
            cls._instance.current_index = 0
            # 
            # ここで部位ごとのインスタンス変数を初期化処理する
            # 
            cls._instance.right_arm = {
                "r_shoulder": np.empty((7, cls._max_frame)),
                "r_uparm": np.empty((7,cls._max_frame)),
                "r_lowarm": np.empty((7,cls._max_frame)), 
                "r_hand": np.empty((7, cls._max_frame))
            }
        return cls._instance
    
    # ここを変更する
    def start(self, db_data_manager):
        if not self.receiver.running:
            self.receiver.start_compare(self.data_queue, self, db_data_manager)
        else:
            raise ValueError("Receiver is already running")
        
    def stop(self):
        if self.receiver.running:
            self.receiver.stop()
        else:
            raise ValueError("Receiver is not running")
    

def get_compare_manager():
    return CompareManager()
