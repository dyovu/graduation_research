

def show_quaternion(data):
    # show_right_hand_quaternion(data)
    show_all_right_arm_quaternion(data)
    pass

# 右手のクォータニオンを出力し続ける
def show_right_hand_quaternion(data):
    right_hand_data = data["fram"]["btrs"][18]["tran"][0:4]
    print(right_hand_data)


# 右腕のクォータニオンを座標ごとに連続で出力する
def show_all_right_arm_quaternion(data):
    right_hand_data = data["fram"]["btrs"]
    tmp_data = [[0] for _ in range(4)]
    for i in range(4):
        tmp_data[i] = right_hand_data[i+15]["tran"][0:4]

    print(tmp_data)