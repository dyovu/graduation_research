from fastapi import (FastAPI, HTTPException, Depends, status)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import uvicorn
import queue
import asyncio
import datetime

from mcp_receiver.receiver import Receiver
from sql_app.database import get_db
from sql_app.put_data import create_data
from service.insert_data import insert_all_data
from service.insert_data import insert_some_data

app = FastAPI()
recv = Receiver()
#すべてのデータが入っているqueueです
data_queue = queue.Queue()

# CORS設定
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/process_data")
async def process_data():
    #もしdata_queueがからでない場合からに初期化したほうがいいかも
    recv.get(data_queue)
    return {"message": "get_process_data"}



@app.get("/stop_put_data")
async def process(db: Session = Depends(get_db)):
    print("stop_put_data")
    recv.stop()

    return insert_all_data(db=db, q = data_queue)



@app.get("/insert_some_data")
async def insertTest(db: Session = Depends(get_db)):
    print("insert_some_data")
    recv.stop()
    
    return insert_some_data(db=db, q = data_queue, n = 1)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
