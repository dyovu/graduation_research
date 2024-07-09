from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import queue
import asyncio
from mcp_receiver.receiver import Receiver
from service.put_data import create_data

app = FastAPI()
recv = Receiver()
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
async def process():
    recv.stop()
    return {"message": "stop_process_data"}




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
