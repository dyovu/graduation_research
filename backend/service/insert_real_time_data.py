import numpy as np

from backend.manager.compare_manager import CompareManager, get_compare_manager
from backend.manager.insertion_manager import InsertionManager, get_insertion_manager

def insert_real_time_data(
    data,
    converted_data,
    insertion_manager: InsertionManager = get_insertion_manager(),
    compare_manager:CompareManager = get_compare_manager(),
):  
    _compare(compare_manager, converted_data)



"""
    Compare用: insertionと同じく腰からの相対位置（x, y, z）と次のフレームまでのベクトル（x, y, z）をいれる
    本番もこれを用いてDPマッチングする
"""
#
# 各振り付けごとに関節データを入れるパターン
#
def _compare(compare_manager, data):
    index = compare_manager.current_index
    print(index)

    for i, value in data.items():
        i = int(i)
        if i <= 5:
            compare_manager.jump[i][index][0:3] = value["world_position"]
            compare_manager.jump[i][index][3:6] = value["vector"]
        elif i <= 10:
            continue
        elif i <= 14:
            # iは11から始まる
            # clap_over_head
            compare_manager.clap_over_head[i-11][index][0:3] = value["world_position"]
            compare_manager.clap_over_head[i-11][index][3:6] = value["vector"]

            # l_arm_and_leg_side
            compare_manager.l_arm_and_leg_side[i-11][index][0:3] = value["world_position"]
            compare_manager.l_arm_and_leg_side[i-11][index][3:6] = value["vector"]
        elif i <= 18:
            # iは15から始まる
            # clap_over_head
            compare_manager.clap_over_head[i-11][index][0:3] = value["world_position"]
            compare_manager.clap_over_head[i-11][index][3:6] = value["vector"]

            # r_arm_and_leg_side
            compare_manager.r_arm_and_leg_side[i-15][index][0:3] = value["world_position"]
            compare_manager.r_arm_and_leg_side[i-15][index][3:6] = value["vector"]
        elif i <= 22:
            # iは19から始まる
            # down_two_times
            compare_manager.down_two_times[i-19][index][0:3] = value["world_position"]
            compare_manager.down_two_times[i-19][index][3:6] = value["vector"]

            # front_back
            compare_manager.front_back[i-19][index][0:3] = value["world_position"]
            compare_manager.front_back[i-19][index][3:6] = value["vector"]

            # l_arm_and_leg_side
            compare_manager.l_arm_and_leg_side[i-15][index][0:3] = value["world_position"]
            compare_manager.l_arm_and_leg_side[i-15][index][3:6] = value["vector"]
        else:
            # iは23から始まる
            # down_two_times
            compare_manager.down_two_times[i-19][index][0:3] = value["world_position"]
            compare_manager.down_two_times[i-19][index][3:6] = value["vector"]

            # front_back
            compare_manager.front_back[i-19][index][0:3] = value["world_position"]
            compare_manager.front_back[i-19][index][3:6] = value["vector"]

            # r_arm_and_leg_side
            compare_manager.r_arm_and_leg_side[i-19][index][0:3] = value["world_position"]
            compare_manager.r_arm_and_leg_side[i-19][index][3:6] = value["vector"]

    compare_manager.current_index += 1



"""
    データ形式は腰からの相対位置（x, y, z）と次のフレームまでのベクトル（x, y, z）
"""
def _receiver(insertion_manager, data):
    index = insertion_manager.current_index
    for i in range(4):
        insertion_manager.time_aligned_left_arm[i][index] = np.concatenate((data[str(11+i)]["world_position"] + data[str(11+i)]["vector"]))
        insertion_manager.time_aligned_right_arm[i][index] = np.concatenate((data[str(15+i)]["world_position"] + data[str(15+i)]["vector"]))
        # print(insertion_manager.time_aligned_right_arm)
        pass
    insertion_manager.current_index += 1



