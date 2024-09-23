from backend.manager.compare_manager import CompareManager

def insert_right_arm(data, compare_manager:CompareManager):
    
    motion_data = data["fram"]["btrs"]
    index = compare_manager.current_index

    #　1回の呼び出しが終わったらindexを1増やす

    for i in range(7):
        compare_manager.right_arm["r_shoulder"][i][index] = motion_data[15]["tran"][i]
        compare_manager.right_arm["r_uparm"][i][index] = motion_data[16]["tran"][i]
        compare_manager.right_arm["r_lowarm"][i][index] = motion_data[17]["tran"][i]
        compare_manager.right_arm["r_hand"][i][index] = motion_data[18]["tran"][i]
    compare_manager.current_index += 1

