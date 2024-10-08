import numpy as np

class DbDataManager:
    _instance = None

    # 今はデータのサイズによって変える
    _right_frame_size = 74
    _left_frame_size = 56

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbDataManager, cls).__new__(cls)
            # 
            # ここで部位ごとのインスタンス変数を初期化処理する
            # 
            # 右手
            cls._instance.right_arm_frame = cls._right_frame_size
            cls._instance.right_arm = [
                np.zeros((7, cls._right_frame_size)),
                np.zeros((7, cls._right_frame_size)),
                np.zeros((7, cls._right_frame_size)),
                np.zeros((7, cls._right_frame_size))
            ]
            # 左手
            cls._instance.left_arm_frame = cls._left_frame_size
            cls._instance.left_arm = [
                np.zeros((7, cls._left_frame_size)),
                np.zeros((7, cls._left_frame_size)),
                np.zeros((7, cls._left_frame_size)),
                np.zeros((7, cls._left_frame_size))
            ]
            # 
            # 時間順に、7つのデータのまとまりとしてcos類似度を計算する
            # 
            cls._instance.left_arm_time = [
                np.zeros((cls._left_frame_size, 7)),
                np.zeros((cls._left_frame_size, 7)),
                np.zeros((cls._left_frame_size, 7)), 
                np.zeros((cls._left_frame_size, 7))
            ]
        return cls._instance


def get_db_data_manager():
    db_manager = DbDataManager()
    print(f"DbDataManager instance: {db_manager}")
    return db_manager
    
