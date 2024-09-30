import numpy as np

class DbDataManager:
    _instance = None

    # 今はデータのサイズによって変える
    _right_frame_size = 74
    _left_frame_size = 56

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbDataManager, cls).__new__(cls)
            cls._instance.right_arm_frame = cls._right_frame_size
            cls._instance.right_arm = {
                "r_shoulder": np.zeros((7, cls._right_frame_size)),
                "r_uparm": np.zeros((7,cls._right_frame_size)),
                "r_lowarm": np.zeros((7,cls._right_frame_size)), 
                "r_hand": np.zeros((7, cls._right_frame_size))
            }
            cls._instance.left_arm_frame = cls._left_frame_size
            cls._instance.left_arm = {
                "l_shoulder": np.zeros((7, cls._left_frame_size)),
                "l_uparm": np.zeros((7,cls._left_frame_size)),
                "l_lowarm": np.zeros((7,cls._left_frame_size)), 
                "l_hand": np.zeros((7, cls._left_frame_size))
            }
        return cls._instance


def get_db_data_manager():
    db_manager = DbDataManager()
    print(f"DbDataManager instance: {db_manager}")
    return db_manager
    
