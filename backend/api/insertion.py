from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import queue

from backend.database import get_db
from backend.mcp_receiver.receiver import Receiver
from backend.service import body_parts

recv = Receiver()
data_queue = queue.Queue()
router = APIRouter(tags=["insertion"])


# ここのエンドポイントはUDP通信の待受を開始する
@router.get(
    "/start_receiv"
)
async def start_receive_data():
    if recv.running:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Receiver is already working",
        )
    recv.start(data_queue)
    return {"message": "Started waiting for data"}


# ここのエンドポイントはUDP通信の待受を停止する
@router.get(
    "/stop_receiv"
)
async def stop_receive_data():
    if not recv.running:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Receiver has already stopped",
        )
    recv.stop()
    return {"message": "Stopped waiting for data"}


# このエンドポイントで取得したデータをDBにいれる
@router.get(
    "/insert_data"
)
async def insert_data_to_db(
    db: Session = Depends(get_db)
):
    body_parts.insert_right_arm(Session, data_queue)

  