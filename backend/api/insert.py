from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import numpy as np

import queue

from backend.database import get_db
from backend.service.read_bvh import read_bvh, parse_motion
from backend.service.insert_bvh import insert_bvh

router = APIRouter(tags=["insert"])


"""
    ！！！！！
    いれたいBVHデータによってここを変更する
    ！！！！！
"""
main_path = 'backend/motion_data/'

file_names = ["clapOverHead", "downTwoTimes", "frontBack", "jump", "LArmAndLegSide", "RArmAndLegSide"]

@router.get(
    "/insert_data"
)
async def insert_data_to_db(
    db: Session = Depends(get_db),
):
    # print("insert_data")
    # for file_name in file_names:
    #     hierarchy_lines, motion_lines = read_bvh(main_path + file_name + ".BVH")
    #     # motion dataの部分を計算する
    #     choreo_data = parse_motion(motion_lines)
    #     print("choreo_data.qsize()", choreo_data.qsize())
        
    #     if choreo_data.empty():
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail="q is empty",
    #         )
        # insert_bvh(db, choreo_data, file_name)

    print("データをれたい場合はコメントアウトを解除してください")
    """
        特定のファイルだけDBに入れたい時
    """
    # file_name = file_names[5]
    # hierarchy_lines, motion_lines = read_bvh(main_path + file_name + ".BVH")
    # # motion dataの部分を計算する
    # choreo_data = parse_motion(motion_lines)
    # print("choreo_data.qsize()", choreo_data.qsize())
    
    # if choreo_data.empty():
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="q is empty",
    #     )
    # insert_bvh(db, choreo_data, file_name)


