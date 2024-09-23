from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import numpy as np
import asyncio
import queue


from backend.database import get_db
from backend.mcp_receiver.receiver import Receiver
from backend.manager.compare_manager import CompareManager, get_compare_manager
from backend.manager.db_data_manager import DbDataManager, get_db_data_manager

router = APIRouter(tags=["compare"])

# 
# DBにデータを入れる際のエンドポイント専用とする
# compare_managerのメソッドを用いてUDP通信の起動と停止をする
# 

# ここのエンドポイントはUDP通信の待受を開始する
@router.get(
    "/start_compare"
)
async def start_receive_data(
    compare_manager: CompareManager = Depends(get_compare_manager),
    db_data_manager: DbDataManager = Depends(get_db_data_manager),
):
    recv:Receiver = compare_manager.receiver
    data_queue:queue.Queue = compare_manager.data_queue

    if recv.running:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Receiver is already working",
        )
    # キューを空にする
    while not data_queue.empty():
        data_queue.get_nowait()

    compare_manager.current_index = 0
    compare_manager.right_arm = {
        "r_shoulder": np.zeros((7, compare_manager._max_frame)),
        "r_uparm": np.zeros((7,compare_manager._max_frame)),
        "r_lowarm": np.zeros((7,compare_manager._max_frame)), 
        "r_hand": np.zeros((7, compare_manager._max_frame))
    }
    
    # print(compare_manager.right_arm["r_shoulder"].shape[1])
    print(compare_manager.right_arm["r_shoulder"][0])
    print(compare_manager.current_index)

    compare_manager.start(db_data_manager)
    # await asyncio.sleep(1)
    # recv.stop()
    return {"message": "Started waiting for data"}


# ここのエンドポイントはUDP通信の待受を停止する
@router.get(
    "/start_compare"
)
async def stop_receive_data(
    compare_manager: CompareManager = Depends(get_compare_manager)
):
    recv:Receiver = compare_manager.receiver

    if not recv.running:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Receiver has already stopped",
        )
    compare_manager.stop()
    print(compare_manager.right_arm["r_shoulder"][0, 0:compare_manager.current_index])
    print(compare_manager.right_arm["r_shoulder"][0, 0:compare_manager.current_index+1])
    print(compare_manager.current_index)
    return {"message": "Stopped waiting for data"}



