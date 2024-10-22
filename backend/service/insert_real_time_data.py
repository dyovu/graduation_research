from backend.manager.compare_manager import CompareManager, get_compare_manager
from backend.manager.insertion_manager import InsertionManager, get_insertion_manager

def insert_real_time_data(
    data,
    converted_data,
    insertion_manager: InsertionManager = get_insertion_manager(),
    compare_manager:CompareManager = get_compare_manager(),
):  
    #　1回の呼び出しが終わったらindexを1増やす
    index_c = compare_manager.current_index
    index_i = insertion_manager.current_index


    '''
        とりあえずDPマッチングやユークリッド距離、cos類似度の比較をする際のデータは時系列のデータになりそう。   
        つまりn行-7列のデータになりそう
        データの種類はクォータニオンと座標値どちらも用いる
    '''
    # こちらの形式で比較を進める
    # converted dataはそもそもnp arrayなのにそれをnp arrayのtime_aligned_left_arm荷入れてる
    for i in range(4):
        insertion_manager.time_aligned_left_arm[i][index_i] = converted_data[str(11+i)]
        insertion_manager.time_aligned_right_arm[i][index_i] = converted_data[str(15+i)]
        # print(insertion_manager.time_aligned_right_arm)
        pass
        
    # print(insertion_manager.time_aligned_right_arm[3][index_i])

    # このデータ形式は今後使わなくなるかもしれない
    # 最終的な比較の際はcompare_managerを変更してn行-7列のデータが入るようにする
    for i in range(4):
        for j in range(7):
            compare_manager.left_arm[i][j][index_c] = data['fram']["btrs"][11+i]["tran"][j]
            compare_manager.right_arm[i][j][index_c] = data['fram']["btrs"][15+i]["tran"][j]

    compare_manager.current_index += 1
    insertion_manager.current_index += 1
    return

