import numpy as np

from backend.manager.compare_manager import CompareManager, get_compare_manager

def insert_real_time_data(
    converted_data,
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
    # print(index)

    for i, value in data.items():
        # print(value["vector"])
        if not isinstance(value["vector"], (np.ndarray)) or len(value["vector"]) != 3:
            print(f"Unexpected vector format at index {i}: {value['vector']}")
            continue
        i = int(i)
        if i <= 5:
            compare_manager.jump[i][index][0:3] = value["world_position"]
            compare_manager.jump[i][index][3:6] = value["vector"]
            if i == 0:
                compare_manager.down_two_times[0][index][0:3] = value["world_position"]
                compare_manager.down_two_times[0][index][3:6] = value["vector"]
                compare_manager.front_back[0][index][0:3] = value["world_position"]
                compare_manager.front_back[0][index][3:6] = value["vector"]
                compare_manager.side_walk[0][index][0:3] = value["world_position"]
                compare_manager.side_walk[0][index][3:6] = value["vector"]
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
            compare_manager.down_two_times[i-18][index][0:3] = value["world_position"]
            compare_manager.down_two_times[i-18][index][3:6] = value["vector"]

            # front_back
            compare_manager.front_back[i-18][index][0:3] = value["world_position"]
            compare_manager.front_back[i-18][index][3:6] = value["vector"]

            compare_manager.side_walk[i-18][index][0:3] = value["world_position"]
            compare_manager.side_walk[i-18][index][3:6] = value["vector"]

            # l_arm_and_leg_side
            compare_manager.l_arm_and_leg_side[i-15][index][0:3] = value["world_position"]
            compare_manager.l_arm_and_leg_side[i-15][index][3:6] = value["vector"]
        else:
            # iは23から始まる
            # down_two_times
            compare_manager.down_two_times[i-18][index][0:3] = value["world_position"]
            compare_manager.down_two_times[i-18][index][3:6] = value["vector"]

            # front_back
            compare_manager.front_back[i-18][index][0:3] = value["world_position"]
            compare_manager.front_back[i-18][index][3:6] = value["vector"]

            # print(f"i={i}, i-18={i-18}, side_walk length={len(compare_manager.side_walk)}")
            # side_walk
            compare_manager.side_walk[i-18][index][0:3] = value["world_position"]
            compare_manager.side_walk[i-18][index][3:6] = value["vector"]

            # r_arm_and_leg_side
            compare_manager.r_arm_and_leg_side[i-19][index][0:3] = value["world_position"]
            compare_manager.r_arm_and_leg_side[i-19][index][3:6] = value["vector"]

    compare_manager.current_index += 1







