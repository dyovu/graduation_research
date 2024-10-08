from backend.manager.compare_manager import CompareManager

def insert_real_time_data(data, compare_manager:CompareManager):

    # print("insert_real_time_data")
    # print("current_index is ", compare_manager.current_index)
    
    motion_data = data["fram"]["btrs"]
    index = compare_manager.current_index

    #　1回の呼び出しが終わったらindexを1増やす

    for i in range(7):
        compare_manager.left_arm[0][i][index] = motion_data[11]["tran"][i]
        compare_manager.left_arm[1][i][index] = motion_data[12]["tran"][i]
        compare_manager.left_arm[2][i][index] = motion_data[13]["tran"][i]
        compare_manager.left_arm[3][i][index] = motion_data[14]["tran"][i]

        compare_manager.right_arm[0][i][index] = motion_data[15]["tran"][i]
        compare_manager.right_arm[1][i][index] = motion_data[16]["tran"][i]
        compare_manager.right_arm[2][i][index] = motion_data[17]["tran"][i]
        compare_manager.right_arm[3][i][index] = motion_data[18]["tran"][i]

    # 各時間におけるデータのまとまりを1つとする
    compare_manager.left_arm_time[0][index] = motion_data[11]["tran"]
    compare_manager.left_arm_time[1][index] = motion_data[12]["tran"]
    compare_manager.left_arm_time[2][index] = motion_data[13]["tran"]
    compare_manager.left_arm_time[3][index] = motion_data[14]["tran"]

    compare_manager.current_index += 1
    return

