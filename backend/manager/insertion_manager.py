# receiver_manager.py
from fastapi import HTTPException, status

import queue
import numpy as np

"""""
このクラスはシングルトンパターン（クラスのインスタンスが1つだけ存在することを保証する）
"""""

class InsertionManager:
    # クラス変数 : クラス内で普遍の変数。いくつインスタンスを作ってもこの値は変わらない。
    _instance = None
    _max_frame = 10000

    # _instanceが存在するかどうか
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InsertionManager, cls).__new__(cls)
            cls._instance.data_queue = queue.Queue()
            from backend.mcp_receiver.receiver import Receiver
            cls.receiver = Receiver()
            cls._instance.current_index = 0
            # 
            # 時間順に、7つのデータのまとまりとしてcos類似度とユークリッド距離を計算するためのデータを入れる配列
            # 
            cls._instance.right_arm_time = [
                np.zeros((cls._max_frame, 7)),
                np.zeros((cls._max_frame, 7)),
                np.zeros((cls._max_frame, 7)), 
                np.zeros((cls._max_frame, 7))
            ]
            cls._instance.left_arm_time = [
                np.zeros((cls._max_frame, 7)),
                np.zeros((cls._max_frame, 7)),
                np.zeros((cls._max_frame, 7)), 
                np.zeros((cls._max_frame, 7))
            ]
        return cls._instance

    def start(self):
        if not self.receiver.running:
            self.receiver.start_insert(self.data_queue)
        else:
            raise ValueError("Receiver is already running")

    def stop(self):
        if self.receiver.running:
            self.receiver.stop()
        else:
            raise ValueError("Receiver is not running")

    def get_data(self):
        return self.data_queue.get() if not self.data_queue.empty() else None
    
    def reset(self):
        while not self.data_queue.empty():
            self.data_queue.get_nowait()
    

def get_insertion_manager():
    return InsertionManager()
