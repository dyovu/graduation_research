from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import numpy as np
import asyncio
import queue


from backend.database import get_db
from backend.mcp_receiver.receiver import Receiver
from backend.manager.insertion_manager import InsertionManager, get_insertion_manager
from backend.manager.compare_manager import CompareManager, get_compare_manager

router = APIRouter(tags=["insertion"])

# 
# DBにデータを入れる際のエンドポイント専用とする
# InsertionManagerのメソッドを用いてUDP通信の起動と停止をする
# 
# ここのエンドポイントはUDP通信の待受を開始する
@router.get(
    "/start_receiv"
)
async def start_receive_data(
    insertion_manager: InsertionManager = Depends(get_insertion_manager),
    compare_manager: CompareManager = Depends(get_compare_manager)
):
    recv:Receiver = insertion_manager.receiver
    data_queue:queue.Queue = insertion_manager.data_queue

    if recv.running:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Receiver is already working",
        )
    # キューを空にする
    while not data_queue.empty():
        data_queue.get_nowait()

    insertion_manager.start(compare_manager)
    return {"message": "Started waiting for data"}


# ここのエンドポイントはUDP通信の待受を停止する
@router.get(
    "/stop_receiv"
)
async def stop_receive_data(
    insertion_manager: InsertionManager = Depends(get_insertion_manager)
):
    recv:Receiver = insertion_manager.receiver

    if not recv.running:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Receiver has already stopped",
        )
    insertion_manager.stop()

    return {"message": "Stopped waiting for data"}


# ---------------------
# body_partsのメソッドを入れ替えることでDBに挿入するデータを変える
# ---------------------

#このエンドポイントで取得したデータをDBにいれる
@router.get(
    "/insert_data"
)
async def insert_data_to_db(
    db: Session = Depends(get_db),
    insertion_manager: InsertionManager = Depends(get_insertion_manager),
):
    q:queue.Queue = insertion_manager.data_queue
    print(q.qsize())
    if q.empty():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="q is empty",
        )
    
    # 右手回転
    # create_body_parts_data.insert_right_arm_turn(db, q)

    # 左手
    print("It does not work")
    # create_body_parts_data.insert_left_arm_turn(db, q)
    return {"message": "Data inserted into the database"}
