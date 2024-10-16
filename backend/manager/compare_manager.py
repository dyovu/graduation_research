# receiver_manager.py

import queue
import numpy as np

"""""
このクラスはシングルトンパターン（クラスのインスタンスが1つだけ存在することを保証する）
"""""

class CompareManager:
    # クラス変数 : クラス内で普遍の変数。いくつインスタンスを作ってもこの値は変わらない。
    _instance = None
    _max_frame = 10000

    # _instanceが存在するかどうか
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CompareManager, cls).__new__(cls)
            from backend.mcp_receiver.receiver import Receiver
            cls.receiver = Receiver() 
            cls._instance.data_queue = queue.Queue()
            cls._instance.current_index = 0
            # 
            # ここで部位ごとのインスタンス変数を初期化処理する
            # 
            # 右手
            cls._instance.right_arm = [
                np.zeros((7, cls._max_frame)),
                np.zeros((7,cls._max_frame)),
                np.zeros((7,cls._max_frame)), 
                np.zeros((7, cls._max_frame))
            ]
            # 左手
            cls._instance.left_arm = [
                np.zeros((7, cls._max_frame)),
                np.zeros((7,cls._max_frame)),
                np.zeros((7,cls._max_frame)), 
                np.zeros((7, cls._max_frame))
            ]
        return cls._instance
    
    # ここを変更する
    def start(self):
        if not self.receiver.running:
            self.receiver.start_compare(self.data_queue)
        else:
            raise ValueError("Receiver is already running")
        
    def stop(self):
        if self.receiver.running:
            self.receiver.stop()
        else:
            raise ValueError("Receiver is not running")
        
        
    def reset(self):
        """CompareManagerの全てのデータをリセット"""
        self.current_index = 0
        self.right_arm = [
            np.zeros((7, self._max_frame)),
            np.zeros((7, self._max_frame)),
            np.zeros((7, self._max_frame)),
            np.zeros((7, self._max_frame))
        ]
        self.left_arm = [
            np.zeros((7, self._max_frame)),
            np.zeros((7, self._max_frame)),
            np.zeros((7, self._max_frame)),
            np.zeros((7, self._max_frame))
        ]
        self.left_arm_time = [
            np.zeros((self._max_frame, 7)),
            np.zeros((self._max_frame, 7)),
            np.zeros((self._max_frame, 7)),
            np.zeros((self._max_frame, 7))
        ]
        # キューを空にする
        while not self.data_queue.empty():
            self.data_queue.get_nowait()
    

def get_compare_manager():
    return CompareManager()
