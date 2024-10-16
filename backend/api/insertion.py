from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import numpy as np
import asyncio
import queue


from backend.database import get_db
from backend.mcp_receiver.receiver import Receiver
from backend.manager.insertion_manager import InsertionManager, get_insertion_manager
from backend.service import create_body_parts_data

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
):
    data_queue:queue.Queue = insertion_manager.data_queue

    # キューを空にする
    while not data_queue.empty():
        data_queue.get_nowait()

    insertion_manager.start()
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
    # create_body_parts_data.insert_left_arm_turn(db, q)
    
    print("It does not work")
    return {"message": "Data inserted into the database"}
