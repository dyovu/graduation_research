from backend.manager.compare_manager import CompareManager, get_compare_manager
from backend.manager.insertion_manager import InsertionManager, get_insertion_manager

def insert_real_time_data(
    data,
    compare_manager:CompareManager = get_compare_manager(),
    insertion_manager: InsertionManager = get_insertion_manager(),
):
    # print("insert_real_time_data")
    # print("current_index is ", compare_manager.current_index)
    
    motion_data = data["fram"]["btrs"]
    index_c = compare_manager.current_index
    index_i = insertion_manager.current_index
    #　1回の呼び出しが終わったらindexを1増やす

    '''
        実際に比較して音を出す際に使用するデータ（現状）
        これから変更になって時間列によるデータの保存に切り替えるかも
        各座標、クォータニオンごとにデータを追加していく
    '''
    for i in range(7):
        compare_manager.left_arm[0][i][index_c] = motion_data[11]["tran"][i]
        compare_manager.left_arm[1][i][index_c] = motion_data[12]["tran"][i]
        compare_manager.left_arm[2][i][index_c] = motion_data[13]["tran"][i]
        compare_manager.left_arm[3][i][index_c] = motion_data[14]["tran"][i]

        compare_manager.right_arm[0][i][index_c] = motion_data[15]["tran"][i]
        compare_manager.right_arm[1][i][index_c] = motion_data[16]["tran"][i]
        compare_manager.right_arm[2][i][index_c] = motion_data[17]["tran"][i]
        compare_manager.right_arm[3][i][index_c] = motion_data[18]["tran"][i]


    '''
        insertする際にそれぞれの座標がどうなっているかcos類似度とユークリッド距離で比較するためのデータ
    '''
    # 各時間におけるデータのまとまりを1つとする
    insertion_manager.left_arm_time[0][index_i] = motion_data[11]["tran"]
    insertion_manager.left_arm_time[1][index_i] = motion_data[12]["tran"]
    insertion_manager.left_arm_time[2][index_i] = motion_data[13]["tran"]
    insertion_manager.left_arm_time[3][index_i] = motion_data[14]["tran"]

    compare_manager.current_index += 1
    insertion_manager.current_index += 1
    return

