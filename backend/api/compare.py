from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import numpy as np
import asyncio
import queue


from backend.database import get_db
from backend.mcp_receiver.receiver import Receiver
from backend.manager.compare_manager import CompareManager, get_compare_manager

router = APIRouter(tags=["compare"])


# --------
# "/start_compare"にアクセスがあった場合にDBからdb_managerにデータを入れる処理をする
# serviceに新しくretrieveの処理を関数化したものを作る
# -------

# 
# DBにデータを入れる際のエンドポイント専用とする
# compare_managerのメソッドを用いてUDP通信の起動と停止をする
# 

@router.get(
    "/start_compare"
)
async def start_receive_data(
    compare_manager: CompareManager = Depends(get_compare_manager),
):
    # recv:Receiver = compare_manager.receiver
    data_queue:queue.Queue = compare_manager.data_queue

    # if recv.running:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Receiver is already working",
    #     )

    compare_manager.reset()

    compare_manager.start()
    return {"message": "Started waiting for data"}


# ここのエンドポイントはUDP通信の待受を停止する
@router.get(
    "/stop_compare"
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
    # print(compare_manager.right_arm["r_shoulder"][0, 0:compare_manager.current_index])
    # print(compare_manager.right_arm["r_shoulder"][0, 0:compare_manager.current_index+1])
    # print(compare_manager.current_index)
    return {"message": "Stopped waiting for data"}



