import numpy as np

class DbDataManager:
    _instance = None
    _frame_size = 50

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbDataManager, cls).__new__(cls)
            cls._instance.right_arm = {
                "r_shoulder": np.empty((7, cls._frame_size)),
                "r_uparm": np.empty((7,cls._frame_size)),
                "r_lowarm": np.empty((7,cls._frame_size)), 
                "r_hand": np.empty((7, cls._frame_size))
            }
            cls._instance.right_arm_frame = cls._frame_size
            return cls._instance


def get_db_data_manager():
    return DbDataManager()
