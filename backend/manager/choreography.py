import numpy as np

class Choreography:

    # 
    def __init__(self, clap_over_hand_size, down_two_times_size, front_back_size, jump_size, l_arm_and_leg_side_size, r_arm_and_leg_side_size):
        self.clap_over_hand = [
            np.zeros((clap_over_hand_size, 7)),
            np.zeros((clap_over_hand_size, 7)),
            np.zeros((clap_over_hand_size, 7)),
            np.zeros((clap_over_hand_size, 7))
        ]
        self.down_two_times = [
            np.zeros((down_two_times_size, 7)),
            np.zeros((down_two_times_size, 7)),
            np.zeros((down_two_times_size, 7)),
            np.zeros((down_two_times_size, 7))
        ]
        self.front_back = [
            np.zeros((front_back_size, 7)),
            np.zeros((front_back_size, 7)),
            np.zeros((front_back_size, 7)),
            np.zeros((front_back_size, 7))
        ]
        self.jump = [
            np.zeros((jump_size, 7)),
            np.zeros((jump_size, 7)),
            np.zeros((jump_size, 7)),
            np.zeros((jump_size, 7))
        ]
        self.front_back = [
            np.zeros((l_arm_and_leg_side_size, 7)),
            np.zeros((l_arm_and_leg_side_size, 7)),
            np.zeros((l_arm_and_leg_side_size, 7)),
            np.zeros((l_arm_and_leg_side_size, 7))
        ]
        self.front_back = [
            np.zeros((r_arm_and_leg_side_size, 7)),
            np.zeros((r_arm_and_leg_side_size, 7)),
            np.zeros((r_arm_and_leg_side_size, 7)),
            np.zeros((r_arm_and_leg_side_size, 7))
        ]