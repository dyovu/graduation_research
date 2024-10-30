import numpy as np

class DbDataManager:
    _instance = None

    # 今はデータのサイズによって変える
    _right_frame_size = 74
    _left_frame_size = 56

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbDataManager, cls).__new__(cls)
            """
                Compare用: insertionと同じく腰からの相対位置（x, y, z）と次のフレームまでのベクトル（x, y, z）をいれる
            """
            cls._instance.time_aligned_right_arm = [
                np.zeros((cls._max_frame, 6)),
                np.zeros((cls._max_frame, 6)),
                np.zeros((cls._max_frame, 6)), 
                np.zeros((cls._max_frame, 6))
            ]
            cls._instance.time_aligned_left_arm = [
                np.zeros((cls._max_frame, 6)),
                np.zeros((cls._max_frame, 6)),
                np.zeros((cls._max_frame, 6)), 
                np.zeros((cls._max_frame, 6))
            ]
        return cls._instance


def get_db_data_manager():
    db_manager = DbDataManager()
    print(f"DbDataManager instance: {db_manager}")
    return db_manager
    
