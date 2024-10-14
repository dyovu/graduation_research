import threading
import time

from scipy.spatial.distance import cosine, euclidean

from backend.manager.compare_manager import CompareManager, get_compare_manager
from backend.dump_data.left_arm.left_arm import bottom_l, front_l, side_l, top_l


right_ram_sample = []


def check_sim():
    compare_left_arm_cos()
    # compare_left_arm_ecu()
    pass


'''
    右腕が右横、前、上、下の状態のx,y,xの相対位置がdump_dataに入っている
    現在の右腕の座標がそれぞれの位置からどれだけ近いか、類似度があるかを毎回出力する
    cos類似度、ユークリッド距離それぞれについて調べる
'''
def compare_right_arm_cos(
    compare_manager:CompareManager = get_compare_manager()
):
    index = compare_manager.current_index
    right_arm = [[0]*4]*4

    for i in range(4):
        for j in range(4):
            cos_bot = 1 - cosine(
                compare_manager.right_arm_time[0][index-1][4:7], 
                right_ram_sample[i][j][4:7]
            )
            bottom[i] = float(cos_bot)




def compare_right_arm_ecu(
    compare_manager:CompareManager = get_compare_manager()
):
    index = compare_manager.current_index






def compare_left_arm_cos(
    compare_manager:CompareManager = get_compare_manager()
):
    index = compare_manager.current_index

    bottom = [0]*4
    front = [0]*4
    side = [0]*4
    top = [0]*4

    for i in range(4):
        cos_bot = 1 - cosine(
            compare_manager.left_arm_time[0][index-1][4:7], 
            bottom_l[i][4:7]
        )
        bottom[i] = float(cos_bot)

        cos_fro = 1 - cosine(
            compare_manager.left_arm_time[1][index-1][4:7],
            front_l[i][4:7]
        )
        front[i] = float(cos_fro)

        cos_sid = 1 - cosine(
            compare_manager.left_arm_time[2][index-1][4:7], 
            side_l[i][4:7]
        )
        side[i] = float(cos_sid)

        cos_top = 1 - cosine(
            compare_manager.left_arm_time[3][index-1][4:7], 
            top_l[i][4:7]
        )
        top[i] = float(cos_top)

    print("index : ", index)
    print("bot", bottom)
    print("front", front)
    print("side", side)
    print("top", top)

def compare_left_arm_ecu(
    compare_manager:CompareManager = get_compare_manager()
):
    index = compare_manager.current_index

    bottom = [0]*4
    front = [0]*4
    side = [0]*4
    top = [0]*4

    for i in range(4):
        print(compare_manager.left_arm_time[0][index-1][4:7])
        ecu_bot = euclidean(
            compare_manager.left_arm_time[0][index-1][4:7], 
            bottom_l[i][0][4:7]
        )
        bottom[i] = float(ecu_bot)

        ecu_fro = euclidean(
            compare_manager.left_arm_time[1][index-1][4:7], 
            front_l[i][0][4:7]
        )
        front[i] = float(ecu_fro)

        ecu_sid = euclidean(
            compare_manager.left_arm_time[2][index-1][4:7], 
            side_l[i][0][4:7]
        )
        side[i] = float(ecu_sid)

        ecu_top = euclidean(
            compare_manager.left_arm_time[3][index-1][4:7], 
            top_l[i][0][4:7]
        )
        top[i] = float(ecu_top)

    print("index : ", index)
    print("bot", bottom)
    print("front", front)
    print("side", side)
    print("top", top)

    