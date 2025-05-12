from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
import backend.schemas.choreography as choreography_schemas
import backend.models.choreography as choreography_models
import backend.models.choreography_pq as choreography_models_pq
import backend.models.choreography_nc as choreography_models_nc
from backend.manager.choreography_manager import ChoreographyManager, get_choreography_manager

router = APIRouter(tags=["retrieve"])

@router.get(
    "/get_db_data",
)
async def get_right_arm_data(
    db: Session = Depends(get_db),
    choreography_manager: ChoreographyManager = Depends(get_choreography_manager),
):
    # type == 0なら補正していないBVHデータ、type == 1なら回転の合成の順序が親×子、それ以外なら通常通り補正した子×親
    type = 1
    print("tyoeは", type, "です")
    if type == 0:
        clap_over_head = db.query(choreography_models_nc.ClapOverHead).all()
        down_two_times = db.query(choreography_models_nc.DownTwoTimes).all()
        front_back = db.query(choreography_models_nc.FrontBack).all()
        jump = db.query(choreography_models_nc.Jump).all()
        l_arm_and_leg_side = db.query(choreography_models_nc.LeftArmAndLegSide).all()
        r_arm_and_leg_side = db.query(choreography_models_nc.RightArmAndLegSide).all()
    elif type == 1:
        clap_over_head = db.query(choreography_models_pq.ClapOverHead).all()
        down_two_times = db.query(choreography_models_pq.DownTwoTimes).all()
        front_back = db.query(choreography_models_pq.FrontBack).all()
        jump = db.query(choreography_models_pq.Jump).all()
        l_arm_and_leg_side = db.query(choreography_models_pq.LeftArmAndLegSide).all()
        r_arm_and_leg_side = db.query(choreography_models_pq.RightArmAndLegSide).all()
        side_walk = db.query(choreography_models_pq.SideWalk).all()
    else:
        clap_over_head = db.query(choreography_models.ClapOverHead).all()
        down_two_times = db.query(choreography_models.DownTwoTimes).all()
        front_back = db.query(choreography_models.FrontBack).all()
        jump = db.query(choreography_models.Jump).all()
        l_arm_and_leg_side = db.query(choreography_models.LeftArmAndLegSide).all()
        r_arm_and_leg_side = db.query(choreography_models.RightArmAndLegSide).all()



    formatted_formatted = [choreography_schemas.ClapOverHeadRead.from_orm(record) for record in clap_over_head]
    formatted_down_two_times = [choreography_schemas.DownTwoTimesRead.from_orm(record) for record in down_two_times]
    formatted_front_back = [choreography_schemas.FrontBackRead.from_orm(record) for record in front_back]
    formatted_jump = [choreography_schemas.JumpRead.from_orm(record) for record in jump]
    formatted_l_arm_and_leg_side = [choreography_schemas.LeftArmAndLegSideRead.from_orm(record) for record in l_arm_and_leg_side]
    formatted_r_arm_and_leg_side = [choreography_schemas.RightArmAndLegSideRead.from_orm(record) for record in r_arm_and_leg_side]
    formatted_side_walk = [choreography_schemas.SideWalkkRead.from_orm(record) for record in side_walk]

    insert_clap_over_head(choreography_manager, formatted_formatted)
    insert_down_two_times(choreography_manager, formatted_down_two_times)
    insert_front_back(choreography_manager, formatted_front_back)
    insert_jump(choreography_manager, formatted_jump)
    insert_l_arm_and_leg_side(choreography_manager, formatted_l_arm_and_leg_side)
    insert_r_arm_and_leg_side(choreography_manager, formatted_r_arm_and_leg_side) 
    insert_side_walk(choreography_manager, formatted_side_walk)  
    return

def insert_clap_over_head(coreography, data_list):
    # print(len(data_list))
    for i, data in enumerate(data_list):
        column_index = 0
        for column_name, value in data.__dict__.items():
            if column_name == "id":
                continue
            coreography.clap_over_head[column_index][i] = value
            column_index += 1

def insert_down_two_times(coreography, data_list):
    for i, data in enumerate(data_list):
        column_index = 0
        for column_name, value in data.__dict__.items():
            if column_name == "id":
                continue
            coreography.down_two_times[column_index][i] = value
            column_index += 1

def insert_front_back(coreography, data_list):
    for i, data in enumerate(data_list):
        column_index = 0
        for column_name, value in data.__dict__.items():
            if column_name == "id":
                continue
            coreography.front_back[column_index][i] = value
            column_index += 1

def insert_jump(coreography, data_list):
    for i, data in enumerate(data_list):
        column_index = 0
        for column_name, value in data.__dict__.items():
            if column_name == "id":
                continue
            coreography.jump[column_index][i] = value
            column_index += 1

def insert_l_arm_and_leg_side(coreography, data_list):
    for i, data in enumerate(data_list):
        column_index = 0
        for column_name, value in data.__dict__.items():
            if column_name == "id":
                continue
            coreography.l_arm_and_leg_side[column_index][i] = value
            column_index += 1

def insert_r_arm_and_leg_side(coreography, data_list):
    for i, data in enumerate(data_list):
        column_index = 0
        for column_name, value in data.__dict__.items():
            if column_name == "id":
                continue
            coreography.r_arm_and_leg_side[column_index][i] = value
            column_index += 1

def insert_side_walk(coreography, data_list):
    for i, data in enumerate(data_list):
        column_index = 0
        for column_name, value in data.__dict__.items():
            if column_name == "id":
                continue
            coreography.side_walk[column_index][i] = value
            column_index += 1

