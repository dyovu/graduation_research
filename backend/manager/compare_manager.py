import queue
import numpy as np

"""""
このクラスはシングルトンパターン（クラスのインスタンスが1つだけ存在することを保証する）
"""""

class CompareManager:
    # クラス変数 : クラス内で普遍の変数。いくつインスタンスを作ってもこの値は変わらない。
    _instance = None
    # fps60でやるつもりだから200秒 = 3分20秒まで一応
    _max_frame = 12000

    # _instanceが存在するかどうか
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CompareManager, cls).__new__(cls)
            cls._instance.data_queue = queue.Queue()
            cls._instance.current_index = 0
            """
                Compare用: insertionと同じく腰からの相対位置（x, y, z）と次のフレームまでのベクトル（x, y, z）をいれる
                各動作ごとにnp配列作ってデータが入ってきた瞬間に分ける方針で
            """
            cls._instance.clap_over_head = cls._instance._initialize_movement_list(8)
            cls._instance.down_two_times = cls._instance._initialize_movement_list(9)
            cls._instance.front_back = cls._instance._initialize_movement_list(9)
            cls._instance.jump = cls._instance._initialize_movement_list(6)
            cls._instance.l_arm_and_leg_side = cls._instance._initialize_movement_list(8)
            cls._instance.r_arm_and_leg_side = cls._instance._initialize_movement_list(8)
            cls._instance.side_walk = cls._instance._initialize_movement_list(9)
        return cls._instance
    
    @staticmethod
    def _initialize_movement_list(size):
        """ sizeで指定した個数の_max_frame行×6列のゼロ行列のリストを作成 """
        return [np.zeros((CompareManager._max_frame, 6)) for _ in range(size)]
    
    def start(self):
        from backend.mcp_receiver.receiver import Receiver
        self.receiver = Receiver() 
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

        self.clap_over_head = self._initialize_movement_list(8)
        self.down_two_times = self._initialize_movement_list(9)
        self.front_back = self._initialize_movement_list(9)
        self.jump = self._initialize_movement_list(6)
        self.l_arm_and_leg_side = self._initialize_movement_list(8)
        self.r_arm_and_leg_side = self._initialize_movement_list(8)
        self.side_walk = self._initialize_movement_list(9)

        # キューを空にする
        while not self.data_queue.empty():
            self.data_queue.get_nowait()
    

def get_compare_manager():
    return CompareManager()
