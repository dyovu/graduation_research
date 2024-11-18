from scipy.spatial.transform import Rotation as R
import numpy as np


"""
    -----------------------------
    このコードは親の回転 × 子の回転の順序で掛け合わせるバージョン
    -----------------------------
"""
def convert_tran_data_pq(data, range_of_motion, previous):
    converted_data = None
    if "skdf" in data:
        # print("skdf")
        pass
    else:
        tran = data["fram"]["btrs"]
        converted_data = apply_quaternion(tran)
        if previous != {}:
            calc_vector(converted_data, previous)
        # calc_body_range(converted_data, range_of_motion)

    return converted_data


# quaternionと親間接の位置から子の座標値をとquaternionを求める
def apply_quaternion(data):
    return_data = {}
    for bone in data:
        bnid = bone["bnid"]
        if bnid == 0:
            return_data[str(bnid)] = {}
            qua = bone["tran"][0:4]
            return_data[str(bnid)]["world_rotation"] = R.from_quat(qua)
            return_data[str(bnid)]["world_position"] = np.array(bone["tran"][4:7])
        else:
            return_data = add_parent_posotion_rotation(bone, return_data)
            pass

    return return_data

# 
# 親関節の位置とquaternionからの子間接の位置、quaternionの合成をする
# 
def add_parent_posotion_rotation(bone, return_data):
    bnid = bone["bnid"]
    qua = bone["tran"][0:4]
    qua = R.from_quat(qua)
    pos = np.array(bone["tran"][4:7])

    if bnid == 11:
        world_rotation = return_data["7"]["world_rotation"]*qua
        world_rotation = normalize(world_rotation)
        world_position = return_data["7"]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 15:
        world_rotation = return_data["7"]["world_rotation"]*qua
        world_rotation = normalize(world_rotation)
        world_position = return_data["7"]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 19:
        world_rotation = return_data["0"]["world_rotation"]*qua
        world_rotation = normalize(world_rotation)
        world_position = return_data["0"]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 23:
        world_rotation = return_data["0"]["world_rotation"]*qua
        world_rotation = normalize(world_rotation)
        world_position = return_data["0"]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)
    else:
        world_rotation = return_data[str(bnid-1)]["world_rotation"]*qua
        world_rotation = normalize(world_rotation)
        world_position = return_data[str(bnid-1)]["world_position"] + return_data[str(bnid-1)]["world_rotation"].apply(pos)

    return_data[str(bnid)] = {}
    return_data[str(bnid)]["world_rotation"] = world_rotation
    return_data[str(bnid)]["world_position"] = world_position
    
    return return_data


# quaternionを正規化して返す
def normalize(qua):
    qua_normalized = qua.as_quat() / np.linalg.norm(qua.as_quat())
    qua = R.from_quat(qua_normalized)

    return qua

# 1つ前の座標と現在の座標がなすベクトルを計算して入れる
def calc_vector(conveted_data, previous):
    for index, value in conveted_data.items():
        a = previous[index]["world_position"]
        b = value["world_position"]
        vec = np.array(b - a)
        previous[index]["vector"] = vec


# 取得した全ての関節の座標値からx, y, zの最大値と最小値を出力する関数
# 各座標のkeyにbnidとその値を入れる
def calc_body_range(data, range_of_motion):
    key_list = ["x_min", "y_min", "z_min", "x_max", "y_max", "z_max"]
    # 空なら、最初なら
    if not range_of_motion["x_min"]:
        for index, key in enumerate(range_of_motion.keys()):
            range_of_motion[key] = ["0", data["0"]["world_position"][(index)%3].tolist()]
    else:
        for bnid, value in data.items():
            pos = value["world_position"]
            for i in range(3):
                if range_of_motion[key_list[i]][1] - pos[i] > 0.01:
                    range_of_motion[key_list[i]] = [bnid, pos[i].tolist()]
                    # print(range_of_motion)
                elif pos[i] - range_of_motion[key_list[i+3]][1] > 0.01:
                    range_of_motion[key_list[i +3]] = [bnid, pos[i].tolist()]
                    # print(range_of_motion)
