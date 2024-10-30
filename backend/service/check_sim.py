from scipy.spatial.distance import cosine, euclidean

from backend.manager.insertion_manager import InsertionManager, get_insertion_manager
# from backend.dump_data.left_arm.left_arm import bottom_l, front_l, side_l, top_l
# from backend.dump_data.right_arm.right_arm import bottom_r, front_r, side_r, top_r


# right_arm_sample = [bottom_r, front_r, side_r, top_r]


def check_sim(
    insertion_manager:InsertionManager = get_insertion_manager()
):
    # compare_right_arm_cos()
    # compare_right_arm_ecu()

    # 1秒に1回だけ呼び出したい時
    if insertion_manager.current_index%60 == 0:
        compare_right_arm_ecu()
        pass
    pass

'''
    現在の右腕の座標がそれぞれの位置からどれだけ近いか、類似度があるかを毎回出力する
    cos類似度、ユークリッド距離それぞれについて調べる

    いままでx,y,zの相対位置でやっていたけど、この相対位置はあまり変化しないらしい。
    クォータニオンの座標と回転を用いてユークリッド距離、cos類似度を出そう

'''
# 
# 各時間における四元数のうち座標を用いて距離を出す
# 
# これができたらDPの値も出してみる
# 
def compare_right_arm_ecu(
    insertion_manager:InsertionManager = get_insertion_manager()
):
    # print(right_arm_sample)
    index = insertion_manager.current_index
    right_arm_ecu = [[0]*4]*4

    for i in range(4):
        for j in range(4):
            data = insertion_manager.time_aligned_right_arm[i][index]
            ecu = euclidean(
                insertion_manager.time_aligned_right_arm[i][index], 
                right_arm_sample[j][i][4:7]
            )
            right_arm_ecu[j][i] = float(ecu)
            # print(right_arm_sample[j][i][4:7])
    
    # print("index : ", index)
    # print("bot", right_arm_ecu[0])
    # print("front", right_arm_ecu[1])
    # print("side", right_arm_ecu[2])
    # print("top", right_arm_ecu[3])

    

# 
# 各時間における四元数だけを用いてcos類似度を出そう
# 
def compare_right_arm_cos(
    insertion_manager:InsertionManager = get_insertion_manager()
):
    index = insertion_manager.current_index
    right_arm_cos = [[0]*4]*4

    for i in range(4):
        for j in range(4):
            cos = 1 - cosine(
                insertion_manager.time_aligned_right_arm[j][index-1][0:4], 
                right_arm_sample[i][j][0:4]
            )
            right_arm_cos[i][j] = float(cos)
    
    print("index : ", index)
    print("bot", right_arm_cos[0])
    print("front", right_arm_cos[1])
    print("side", right_arm_cos[2])
    print("top", right_arm_cos[3])