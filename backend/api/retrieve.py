from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
import backend.schemas.choreography as choreography_schemas
import backend.models.choreography as choreography_models
from backend.manager.choreography_manager import ChoreographyManager, get_choreography_manager

router = APIRouter(tags=["retrieve"])

@router.get(
    "/get_db_data",
)
async def get_right_arm_data(
    db: Session = Depends(get_db),
    choreography_manager: ChoreographyManager = Depends(get_choreography_manager),
):
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

    insert_clap_over_head(choreography_manager, formatted_formatted)
    insert_down_two_times(choreography_manager, formatted_down_two_times)
    insert_front_back(choreography_manager, formatted_front_back)
    insert_jump(choreography_manager, formatted_jump)
    insert_l_arm_and_leg_side(choreography_manager, formatted_l_arm_and_leg_side)
    insert_r_arm_and_leg_side(choreography_manager, formatted_r_arm_and_leg_side)  
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

