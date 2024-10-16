from backend.manager.compare_manager import CompareManager, get_compare_manager
from backend.manager.insertion_manager import InsertionManager, get_insertion_manager

def insert_real_time_data(
    data,
    compare_manager:CompareManager = get_compare_manager(),
    insertion_manager: InsertionManager = get_insertion_manager()
):  
    motion_data = data["fram"]["btrs"]
    #　1回の呼び出しが終わったらindexを1増やす
    index_c = compare_manager.current_index
    index_i = insertion_manager.current_index


    '''
        とりあえずDPマッチングやユークリッド距離、cos類似度の比較をする際のデータは時系列のデータになりそう。   
        つまりn行-7列のデータになりそう
        データの種類はクォータニオンと座標値どちらも用いる
    '''
    # こちらの形式で比較を進める
    for i in range(4):
        insertion_manager.left_arm_time[i][index_i] = motion_data[11+i]["tran"]

    # このデータ形式は今後使わなくなるかもしれない
    #
    # 最終的な比較の際はcompare_managerを変更してn行-7列のデータが入るようにする
    #
    for i in range(7):
        for j in range(4):
            compare_manager.left_arm[j][i][index_c] = motion_data[11+j]["tran"][i]
            compare_manager.right_arm[j][i][index_c] = motion_data[15+j]["tran"][i]

    compare_manager.current_index += 1
    insertion_manager.current_index += 1
    return

