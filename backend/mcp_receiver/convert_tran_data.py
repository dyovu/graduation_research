
# 
# 全てのtranデータをこし間接を基準とした1つの座標系の相対位置に変換する
# mocopiのtranに含まれる座標値は親関節からの相対座標になる、親関節から順位座標値を全て足し合わせればok?
# 
"""
    この座標値でユークリッド距離とcos類似度を出してみる
    これでうまくいきそうならDBに保存するデータもこの形にする
    DBにはtran情報だけでいいから他全て切り捨てるかも
"""
# 
# 親関節の位置を順に足し合わせたtranデータのみを返します。
# 
def add_parent_posotion(tran):
    return_data = {}
    for index, bndt in enumerate(tran):
        tmp_list = [0]*7
        if index == 0:
            pass
            # これ以降はどこかしらの親関節の位置に足し合わせていく
        elif index == 11:
            tmp_list[4:7] = return_data["7"][4:7]
        elif index == 15:
            tmp_list[4:7] = return_data["7"][4:7]
        elif index == 19:
            tmp_list[4:7] = return_data["0"][4:7]
        elif index == 23:
            tmp_list[4:7] = return_data["0"][4:7]
        else:
            tmp_list[4:7] = return_data[str(index-1)][4:7]
        return_data[str(index)] = [a+b for a, b in zip(bndt['tran'],tmp_list)]
    
    return return_data


def convert_tran_data(data):
    conveted_data = {}
    
    if "skdf" in data:
        pass
    else:
        tran = data['fram']["btrs"]
        conveted_data = add_parent_posotion(tran)

    return conveted_data