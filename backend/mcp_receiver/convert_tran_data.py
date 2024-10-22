from scipy.spatial.transform import Rotation as R
import numpy as np


"""
    このコードはdeserializeされたframeを受け取りすべての関節をHip(bnid: 0)からの相対位置に変換する
    quaternionを用いた計算方法やスケルトンの構造等はnotionへをみる
"""
# 外部から呼び出される関数
def convert_tran_data(data, range_of_motion):
    conveted_data = {}
    if "skdf" in data:
        pass
    else:
        tran = data['fram']["btrs"]
        conveted_data = apply_quaternion(tran)
    calc_body_range(conveted_data, range_of_motion)

    return conveted_data


# quaternionと親間接の位置から子の座標値をとquaternionを求める
def apply_quaternion(data):
    return_data = {}
    for bone in data:
        bnid = bone["bnid"]
        if bnid == 0:
            return_data[str(bnid)]["world_rotation"] = R.from_quat(bone["tran"][0:4])
            return_data[str(bnid)]["world_position"] = np.array(bone["tran"][4:7])
        else:
            return_data = add_parent_posotion(bone, return_data)

    return return_data

# 
# 親関節の位置を順に足し合わせたtranデータのみを返します。
# 
def add_parent_posotion(bone, return_data):
    bnid = bone["bnid"]
    qua = R.from_quat(bone["tran"][0:4])
    pos = np.array(bone["tran"][4:7])

    tmp_list = [0]*3

    if bnid == 11:
        world_rotation = qua*return_data["7"]["world_rotation"]
        world_position = return_data["7"]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 15:
        world_rotation = qua*return_data["7"]["world_rotation"]
        world_position = return_data["7"]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 19:
        world_rotation = qua*return_data["0"]["world_rotation"]
        world_position = return_data["0"]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 23:
        world_rotation = qua*return_data["0"]["world_rotation"]
        world_position = return_data["0"]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)
    else:
        world_rotation = qua*return_data[str(bnid-1)]["world_rotation"]
        world_position = return_data[str(bnid-1)]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)

    return_data[str(bnid)]["world_rotation"] = world_rotation
    return_data[str(bnid)]["world_position"] = world_position
    
    return return_data



# 取得した全ての関節の座標値からx, y, zの最大値と最小値を出力する関数
# 各座標のkeyにbnidとその値を入れる

def calc_body_range(data, range_of_motion):
    key_list = ["x_min", "y_min", "z_min", "x_max", "y_max", "z_max"]
    # 空なら、最初なら
    if not range_of_motion["x_min"]:
        for index, key in enumerate(range_of_motion.keys()):
            range_of_motion[key] = ["0", data["0"]["world_position"][(index)%3].tolist()]
        print(range_of_motion)
    else:
        for bnid, value in data.items():
            pos = value["world_position"]
            for i in range(3):
                if pos[i] < range_of_motion[key_list[i]][1]:
                    range_of_motion[key_list[i]] = [bnid, pos[i]]
                    print(range_of_motion)
                elif pos[i] > range_of_motion[key_list[i+3]][1]:
                    range_of_motion[key_list[i +3]] = [bnid, pos[i]]
                    print(range_of_motion)
