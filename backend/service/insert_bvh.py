import queue
import logging
import re
from typing import Optional

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

import backend.schemas.choreography as choreography_schemas
import backend.models.choreography as choreography_models

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
    この関数で呼び出す関数を書き換えて入れるデータを変えよう
"""
def insert_bvh(db: Session, q: queue.Queue, file_name):
    # print("insert_bvh")
    match file_name:
        case "clapOverHead":
            insert_clap_over_head(db, q, file_name)
        case "downTwoTimes":
            insert_down_two_times(db, q, file_name)
        case "frontBack":
            insert_front_back(db, q, file_name)
        case "jump":
            insert_jump(db, q, file_name)
        case "LArmAndLegSide":
            insert_l_arm_and_leg_side(db, q, file_name)
        case "RArmAndLegSide":
            insert_r_arm_and_leg_side(db, q, file_name)
    
    

#
# 両手を頭の上で叩く動作
#
def insert_clap_over_head(db: Session, q: queue.Queue, file_name):
    print("insert_clap_over_head")
    db_objs = []
    count = 0

    check_name_match(file_name, choreography_models.ClapOverHead.__tablename__)
    
    while not q.empty():
        insert_data = _create_clap_over_head(q)
        # if(count == 1):
        #     print(insert_data)
        db_obj = choreography_models.ClapOverHead(**insert_data.dict())
        db_objs.append(db_obj)
        count += 1

    db.bulk_save_objects(db_objs)
    db.commit()

def _create_clap_over_head(q: queue.Queue):
    tmp_data = q.get()
    data_dict ={}
    columns = ["l_shoulder", "l_uparm", "l_lowarm", "l_hand", "r_shoulder", "r_uparm", "r_lowarm", "r_hand"]

    for i in range(8):
        pos = tmp_data[str(i+11)]["world_position"].tolist()
        vec = tmp_data[str(i+11)]["vector"].tolist()
        data_dict[columns[i]] = pos + vec
    return choreography_schemas.ClapOverHeadCreate(**data_dict)

#
# 両足を胸に近づける動作
#
def insert_down_two_times(db: Session, q: queue.Queue, file_name):
    print("insert_down_two_times")
    db_objs = []
    count = 0

    check_name_match(file_name, choreography_models.DownTwoTimes.__tablename__)

    while not q.empty():
        insert_data = _create_down_two_times(q)
        # if(count == 1):
        #     print(insert_data)
        db_obj = choreography_models.DownTwoTimes(**insert_data.dict())
        db_objs.append(db_obj)
        count += 1

    db.bulk_save_objects(db_objs)
    db.commit()

def _create_down_two_times(q: queue.Queue):
    tmp_data = q.get()
    data_dict ={}
    columns = ["root", "l_up_leg", "l_low_leg", "l_foot", "l_toes", "r_up_leg", "r_low_leg", "r_foot", "r_toes"]

    pos = tmp_data["0"]["world_position"].tolist()
    vec = tmp_data["0"]["vector"].tolist()
    data_dict[columns[0]] = pos + vec

    for i in range(8):
        pos = tmp_data[str(i+19)]["world_position"].tolist()
        vec = tmp_data[str(i+19)]["vector"].tolist()
        data_dict[columns[i+1]] = pos + vec
    return choreography_schemas.DownTwoTimesCreate(**data_dict)


#
# 1歩前、1歩後ろに動く動作
#
def insert_front_back(db: Session, q: queue.Queue, file_name):
    print("insert_front_back")
    db_objs = []
    count = 0

    check_name_match(file_name, choreography_models.FrontBack.__tablename__)

    while not q.empty():
        insert_data = _create_front_back(q)
        # if(count == 1):
        #     print(insert_data)
        db_obj = choreography_models.FrontBack(**insert_data.dict())
        db_objs.append(db_obj)
        count += 1

    db.bulk_save_objects(db_objs)
    db.commit()

def _create_front_back(q: queue.Queue):
    tmp_data = q.get()
    data_dict ={}
    columns = ["root", "l_up_leg", "l_low_leg", "l_foot", "l_toes", "r_up_leg", "r_low_leg", "r_foot", "r_toes"]

    pos = tmp_data["0"]["world_position"].tolist()
    vec = tmp_data["0"]["vector"].tolist()
    data_dict[columns[0]] = pos + vec

    for i in range(8):
        pos = tmp_data[str(i+19)]["world_position"].tolist()
        vec = tmp_data[str(i+19)]["vector"].tolist()
        data_dict[columns[i+1]] = pos + vec
    return choreography_schemas.FrontBackCreate(**data_dict)


#
# ジャンプ
#
def insert_jump(db: Session, q: queue.Queue, file_name):
    print("insert_jump")
    db_objs = []
    count = 0

    check_name_match(file_name, choreography_models.Jump.__tablename__)

    while not q.empty():
        insert_data = _create_jump(q)
        # if(count == 1):
        #     print(insert_data)
        db_obj = choreography_models.Jump(**insert_data.dict())
        db_objs.append(db_obj)
        count += 1

    db.bulk_save_objects(db_objs)
    db.commit()

def _create_jump(q: queue.Queue):
    tmp_data = q.get()
    data_dict ={}
    columns = ["root", "torso_1", "torso_2", "torso_3", "torso_4", "torso_5"]

    for i in range(6):
        pos = tmp_data[str(i)]["world_position"].tolist()
        vec = tmp_data[str(i)]["vector"].tolist()
        data_dict[columns[i]] = pos + vec
    return choreography_schemas.JumpCreate(**data_dict)


#
# 左手と左足を同時に横に出す
#
def insert_l_arm_and_leg_side(db: Session, q: queue.Queue, file_name):
    print("insert_l_arm_and_leg_side")
    db_objs = []
    count = 0

    check_name_match(file_name, choreography_models.LeftArmAndLegSide.__tablename__)

    while not q.empty():
        insert_data = _create_l_arm_and_leg_side(q)
        # if(count == 1):
        #     print(insert_data)
        db_obj = choreography_models.LeftArmAndLegSide(**insert_data.dict())
        db_objs.append(db_obj)
        count += 1

    db.bulk_save_objects(db_objs)
    db.commit()

def _create_l_arm_and_leg_side(q: queue.Queue):
    tmp_data = q.get()
    data_dict ={}
    columns = ["l_shoulder", "l_uparm", "l_lowarm", "l_hand", "l_up_leg", "l_low_leg", "l_foot", "l_toes"]

    for i in range(4):
        pos = tmp_data[str(i+11)]["world_position"].tolist()
        vec = tmp_data[str(i+11)]["vector"].tolist()
        data_dict[columns[i]] = pos + vec

        pos = tmp_data[str(i+19)]["world_position"].tolist()
        vec = tmp_data[str(i+19)]["vector"].tolist()
        data_dict[columns[i+4]] = pos + vec
    return choreography_schemas.LeftArmAndLegSideCreate(**data_dict)


#
# 右手と右足を同時に横に出す
#
def insert_r_arm_and_leg_side(db: Session, q: queue.Queue, file_name):
    print("insert_r_arm_and_leg_side")
    db_objs = []
    count = 0

    check_name_match(file_name, choreography_models.RightArmAndLegSide.__tablename__)

    while not q.empty():
        insert_data = _create_r_arm_and_leg_side(q)
        # if(count == 1):
        #     print(insert_data)
        db_obj = choreography_models.RightArmAndLegSide(**insert_data.dict())
        db_objs.append(db_obj)
        count += 1

    db.bulk_save_objects(db_objs)
    db.commit()

def _create_r_arm_and_leg_side(q: queue.Queue):
    tmp_data = q.get()
    data_dict ={}
    columns = ["r_shoulder", "r_uparm", "r_lowarm", "r_hand", "r_up_leg", "r_low_leg", "r_foot", "r_toes"]

    for i in range(4):
        pos = tmp_data[str(i+15)]["world_position"].tolist()
        vec = tmp_data[str(i+15)]["vector"].tolist()
        data_dict[columns[i]] = pos + vec

        pos = tmp_data[str(i+23)]["world_position"].tolist()
        vec = tmp_data[str(i+23)]["vector"].tolist()
        data_dict[columns[i+4]] = pos + vec
    return choreography_schemas.RightArmAndLegSideCreate(**data_dict)
















def check_name_match(file_name, model_name):
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', file_name).lower()
    if name != model_name:
        error_message = "テーブル名とBVHのファイル名が一致しません"
        logger.error(f"{error_message}: expected {model_name}, got {name}")
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_message,
        )