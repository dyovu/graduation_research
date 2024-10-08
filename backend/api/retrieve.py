from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import numpy as np

from backend.database import get_db
import backend.schemas.body_parts as body_parts_schemas
import backend.models.body_parts as body_parts_models
from backend.manager.db_data_manager import DbDataManager, get_db_data_manager

router = APIRouter(tags=["retrieve"])

@router.get(
    "/get_right_arm",
    # response_model = list[body_parts_schemas.RightArmRead],
)
async def get_right_arm_data(
    db: Session = Depends(get_db),
    db_data_manager: DbDataManager = Depends(get_db_data_manager),
):
    skip = 0
    limit_r = db_data_manager.right_arm_frame
    limit_l = db_data_manager.left_arm_frame

    # 右手
    raw_data_right_arm = db.query(body_parts_models.RightArmTurn).offset(skip).limit(limit_r).all()
    if not raw_data_right_arm:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    formatted_right_arm_data = [body_parts_schemas.RightArmRead.from_orm(record) for record in raw_data_right_arm]
    # データを変換してDbDataManagerに適用
    transform_right_arm_data(db_data_manager, formatted_right_arm_data)


    # 左手
    raw_data_left_arm = db.query(body_parts_models.LeftArmTurn).offset(skip).limit(limit_l).all()
    if not raw_data_left_arm:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    formatted_left_arm_data = [body_parts_schemas.LeftArmRead.from_orm(record) for record in raw_data_left_arm]
    # データを変換してDbDataManagerに適用
    transform_left_arm_data(db_data_manager, formatted_left_arm_data)

    transform_left_arm_time_data(db_data_manager, formatted_left_arm_data)


    print(db_data_manager.right_arm)
    print("data size of r arm: ", db_data_manager.right_arm_frame)
    print()
    print(db_data_manager.left_arm)
    print()
    print(db_data_manager.left_arm_time)
    print("data size of l arm: ", db_data_manager.left_arm_frame)
    

    return 


def transform_right_arm_data(db_data_manager, data_list):
    # r_shoulder, r_uparm, r_lowarm, r_handのデータをNumPy配列に変換してDbDataManagerにセット
    db_data_manager.right_arm[0] = np.array([data.r_shoulder for data in data_list]).T
    db_data_manager.right_arm[1] = np.array([data.r_uparm for data in data_list]).T
    db_data_manager.right_arm[2] = np.array([data.r_lowarm for data in data_list]).T
    db_data_manager.right_arm[3] = np.array([data.r_hand for data in data_list]).T

def transform_left_arm_data(db_data_manager, data_list):
    # r_shoulder, r_uparm, r_lowarm, r_handのデータをNumPy配列に変換してDbDataManagerにセット
    db_data_manager.left_arm[0] = np.array([data.l_shoulder for data in data_list]).T
    db_data_manager.left_arm[1] = np.array([data.l_uparm for data in data_list]).T
    db_data_manager.left_arm[2] = np.array([data.l_lowarm for data in data_list]).T
    db_data_manager.left_arm[3] = np.array([data.l_hand for data in data_list]).T


# 時間ごとの配列の組みをそれぞれの部位に入れていく
def transform_left_arm_time_data(db_data_manager, data_list):
    for i, data in enumerate(data_list):
        # 各部位のデータを行として追加
        db_data_manager.left_arm_time[0][i] = data.l_shoulder
        db_data_manager.left_arm_time[1][i] = data.l_uparm     
        db_data_manager.left_arm_time[2][i] = data.l_lowarm     
        db_data_manager.left_arm_time[3][i] = data.l_hand
