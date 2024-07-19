from fastapi import (FastAPI, HTTPException, Depends, status)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import uvicorn
import queue
import asyncio

from mcp_receiver.receiver import Receiver
from sql_app.database import get_db
from service.put_data import create_data

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

# データを非同期で収集する関数
async def collect_data(data_queue, duration):
    collected_data = []
    end_time = asyncio.get_event_loop().time() + duration
    
    while asyncio.get_event_loop().time() < end_time:
        try:
            data = data_queue.get_nowait()
            collected_data.append(data)
        except queue.Empty:
            await asyncio.sleep(0.1)
    
    return collected_data


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
    recv.stop()

    tmp_queue = data_queue.get()
    insert_data = {'id': 1, 'uttm':tmp_queue['fram']['time'], 'bnid': tmp_queue['fram']['btrs'][0]['bnid'], 'tran': tmp_queue['fram']['btrs'][0]['tran']}
    #　timeはdatetime型ではないので多分エラーになる、ちゃんとデコードしてdatetime入れよう

    test_data = {'id': 0, 'uttm': '2024-07-10 10:10:10', 'bnid': 2, 'tran': (-0.02605356276035309, 0.6850966215133667, 0.03665921464562416, 0.7270625233650208, 0.015477052889764309, 0.9299008846282959, -0.6536895632743835)}


    print(test_data)
    print(test_data)
    
    # return create_data(db=db, alldata = insert_data)


@app.get("/insert_data_test")
async def insertTest(db: Session = Depends(get_db)):
    test_data = {'id': 0, 'uttm': '2024-07-10 10:10:10', 'bnid': 2, 'tran': (-0.02605356276035309, 0.6850966215133667, 0.03665921464562416, 0.7270625233650208, 0.015477052889764309, 0.9299008846282959, -0.6536895632743835)}

    # return "working"
    return create_data(db=db, alldata = test_data)
    



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
