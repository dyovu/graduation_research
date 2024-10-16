from fastapi import Depends
from scipy.spatial.distance import cosine, euclidean

from backend.manager.insertion_manager import InsertionManager, get_insertion_manager
from backend.dump_data.left_arm.left_arm import bottom_l, front_l, side_l, top_l


right_ram_sample = []


def check_sim():
    compare_right_arm_cos()
    compare_right_arm_ecu()
    pass

'''
    現在の右腕の座標がそれぞれの位置からどれだけ近いか、類似度があるかを毎回出力する
    cos類似度、ユークリッド距離それぞれについて調べる

    いままでx,y,zの相対位置でやっていたけど、この相対位置はあまり変化しないらしい。
    クォータニオンの座標と回転を用いてユークリッド距離、cos類似度を出そう

'''
# 
# 各時間における四元数だけを用いてcos類似度を出そう
# 
def compare_right_arm_cos(
    insertion_manager:InsertionManager = Depends(get_insertion_manager)
):
    index = insertion_manager.current_index
    right_arm_cos = [[0]*4]*4

    for i in range(4):
        for j in range(4):
            cos = 1 - cosine(
                insertion_manager.right_arm_time[j][index-1][0:4], 
                right_ram_sample[i][j][0:4]
            )
            right_arm_cos[i][j] = float(cos)
    
    print("index : ", index)
    print("bot", right_arm_cos[0])
    print("front", right_arm_cos[1])
    print("side", right_arm_cos[2])
    print("top", right_arm_cos[3])

# 
# 各時間における四元数のうち座標を用いて距離を出す
# 
def compare_right_arm_ecu(
    insertion_manager:InsertionManager = Depends(get_insertion_manager)
):
    index = insertion_manager.current_index
    right_arm_ecu = [[0]*4]*4

    for i in range(4):
        for j in range(4):
            ecu = euclidean(
                insertion_manager.right_arm_time[j][index-1][0:3], 
                right_ram_sample[i][j][0:3]
            )
            right_arm_ecu[i] = float(ecu)
    
    print("index : ", index)
    print("bot", right_arm_ecu[0])
    print("front", right_arm_ecu[1])
    print("side", right_arm_ecu[2])
    print("top", right_arm_ecu[3])

    