import numpy as np

# これもシングルトンパターン
class ChoreographyManager:
    _instance = None
    _clap_over_head_size = 74
    _down_two_times_size = 185
    _front_back_size = 166
    _jump_size = 81
    _l_arm_and_leg_side_size = 124
    _r_arm_and_leg_side_size = 99
    _side_walk = 223


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
            cls._instance.side_walk = cls._instance._initialize_movement_list(cls._side_walk, 9)
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
            case "s":
                return cls._side_walk
            
    def is_empty(self):
        if self.clap_over_head[0][4] and self.clap_over_head[1][45] and self.clap_over_head[3][17]:
            return False
        else:
            return True
    

def get_choreography_manager():
    choreography_manager = ChoreographyManager()
    return choreography_manager