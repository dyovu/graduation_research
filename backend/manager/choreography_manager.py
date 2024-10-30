import numpy as np

# これもシングルトンパターン
class ChoreographyManager:
    _instance = None
    _clap_over_head_size = 75
    _down_two_times_size = 186
    _front_back_size = 167
    _jump_size = 82
    _l_arm_and_leg_side_size = 125
    _r_arm_and_leg_side_size = 100


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChoreographyManager, cls).__new__(cls)
            # インスタンス変数を初期化
            cls._instance.clap_over_head = cls._instance._initialize_movement_list(cls._instance._clap_over_head_size, 8)
            cls._instance.down_two_times = cls._instance._initialize_movement_list(cls._down_two_times_size, 9)
            cls._instance.front_back = cls._instance._initialize_movement_list(cls._front_back_size, 9)
            cls._instance.jump = cls._instance._initialize_movement_list(cls._jump_size, 6)
            cls._instance.l_arm_and_leg_side = cls._instance._initialize_movement_list(cls._l_arm_and_leg_side_size, 8)
            cls._instance.r_arm_and_leg_side = cls._instance._initialize_movement_list(cls._r_arm_and_leg_side_size, 8)
        return cls._instance
    
    @staticmethod
    def _initialize_movement_list(row, size):
        """ sizeで指定した個数のrow行×6列のゼロ行列のリストを作成 """
        return [np.zeros((row, 6)) for _ in range(size)]
    
    def return_size(cls, n):
        match n:
            case "c":
                return cls._clap_over_head_size
            case "d":
                return cls._down_two_times_size
            case "f":
                return cls._front_back_size
            case "j":
                return cls._jump_size
            case "l":
                return cls._l_arm_and_leg_side_size
            case "r":
                return cls._r_arm_and_leg_side_size
    

def get_choreography_manager():
    choreography_manager = ChoreographyManager()
    print(f"Choreography instance: {choreography_manager}")
    return choreography_manager