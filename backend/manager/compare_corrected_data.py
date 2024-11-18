import numpy as np

class CompareCorrectDataManager:
    # クラス変数 : クラス内で普遍の変数。いくつインスタンスを作ってもこの値は変わらない。
    _instance = None
    # fps60でやるつもりだから200秒 = 3分20秒まで一応
    _max_frame = 12000

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CompareCorrectDataManager, cls).__new__(cls)
            cls._instance.current_index = 0
            """
                Compare用: insertionと同じく腰からの相対位置（x, y, z）と次のフレームまでのベクトル（x, y, z）をいれる
                各動作ごとにnp配列作ってデータが入ってきた瞬間に分ける方針で
            """
            joint_names = [
                "hip", "torso_1", "torso_2", "torso_3", "torso_4", "torso_5", "torso_6", "torso_7",
                "neck_1", "neck_2", "head", "l_shoulder", "l_up_arm", "l_low_arm", "l_hand",
                "r_shoulder", "r_up_arm", "r_low_arm", "r_hand", "l_up_leg", "l_low_leg",
                "l_foot", "l_toes", "r_up_leg", "r_low_leg", "r_foot", "r_toes"
            ]
            cls._instance.joints = {}
            for name in joint_names:
                cls._instance.joints[name] = cls._instance._initialize_movement_list(7)
        return cls._instance
    
    
    @staticmethod
    def _initialize_movement_list(size):
        """ sizeで指定した個数の_max_frame行×6列のゼロ行列のリストを作成 """
        return [np.zeros((CompareCorrectDataManager._max_frame, 6)) for _ in range(size)]
    

def get_compare_correct_data_manager():
    return CompareCorrectDataManager()