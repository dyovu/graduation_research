import re
import queue

from scipy.spatial.transform import Rotation as R
import numpy as np


# BVHファイルの読み込み
def read_bvh(file_path):
    # print("read_bvh")
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    hierarchy_section = []
    motion_section = []
    is_motion = False
    
    for line in lines:
        if "MOTION" in line:
            is_motion = True
        elif is_motion:
            motion_section.append(line)
        else:
            hierarchy_section.append(line)
    
    return hierarchy_section, motion_section


# motionの各行を読み込んで判別
def parse_motion(lines):
    # print("parse_motion")
    count = 0
    choreo_data = queue.Queue()
    transformed_motion_data = {}
    previous = {}
    frame = None
    for line in lines:
        if line.startswith("Frames:"):
            frame = (int)(line.split()[1])
            print("frame", frame)
        elif line.startswith("Frame Time:"):
            continue
        else:
            transformed_motion_data = calc_relative_position(line)
            if not previous == {}:
                calc_vector(transformed_motion_data, previous)
                choreo_data.put(previous)
                # if count ==10:
                #     print(previous)
            previous = transformed_motion_data
            count += 1
            
    return choreo_data


# motionの各行を解析してpositionとquaterninoに変換、単位もmに変換、convet_tran_dataと同じ形に変換する
def calc_relative_position(line):
    transformed_motion_data = {}
    index = 0
    for i in range(27):
        tmp = {}
        local_pos = np.array([float(x) * 0.01 for x in line.split()[index: index+3]])
        local_eul = [float(x) for x in line.split()[index+3: index+6]]
        rotation = R.from_euler('xyz', local_eul, degrees=True)
        local_qua = R.from_quat(rotation.as_quat())
        """
            今はまだnparray型になってる、DBに入れるのにりつとに戻すならtolist()する
        """
        if i == 0:
            tmp["world_position"] = local_pos
            tmp["world_rotation"] = local_qua
        else:
            tmp = add_parent_posotion_rotation(i, local_pos, local_qua, transformed_motion_data)

        transformed_motion_data[str(i)] = tmp
        index += 6
    
    
    return transformed_motion_data


# 親のquaternionとpositionからこの相対位置を計算する
def add_parent_posotion_rotation(bnid, local_pos, local_qua, parents_data):
    return_data = {}
    bnid = bnid
    pos = local_pos
    qua = local_qua

    if bnid == 11:
        world_rotation = qua * parents_data["7"]["world_rotation"]
        world_rotation = normalize(world_rotation)
        world_position = parents_data["7"]["world_position"] + parents_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 15:
        world_rotation = qua * parents_data["7"]["world_rotation"]
        world_rotation = normalize(world_rotation)
        world_position = parents_data["7"]["world_position"] + parents_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 19:
        world_rotation = qua * parents_data["0"]["world_rotation"]
        world_rotation = normalize(world_rotation)
        world_position = parents_data["0"]["world_position"] + parents_data[str(bnid-1)]["world_rotation"].apply(pos)
    elif bnid == 23:
        world_rotation = qua * parents_data["0"]["world_rotation"]
        world_rotation = normalize(world_rotation)
        world_position = parents_data["0"]["world_position"] + parents_data[str(bnid-1)]["world_rotation"].apply(pos)
    else:
        world_rotation = qua * parents_data[str(bnid-1)]["world_rotation"]
        world_rotation = normalize(world_rotation)
        world_position = parents_data[str(bnid-1)]["world_position"] + parents_data[str(bnid-1)]["world_rotation"].apply(pos)

    return_data["world_rotation"] = world_rotation
    return_data["world_position"] = world_position
    
    return return_data


# quaternionを正規化して返す
def normalize(qua):
    qua_normalized = qua.as_quat() / np.linalg.norm(qua.as_quat())
    qua = R.from_quat(qua_normalized)

    return qua

def calc_vector(conveted_data, previous):
    for index, value in conveted_data.items():
        a = previous[index]["world_position"]
        b = value["world_position"]
        vec = b - a
        previous[index]["vector"] = vec


# 使用例
"""
    file_path = 'clapOverHead.BVH'

    hierarchy_lines, motion_lines = read_bvh(file_path)

    # motion dataの部分を計算する
    parse_motion(motion_lines)
"""

