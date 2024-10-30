import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 
# ここにAPIのエンドポイントとなるファイルを追加していく
# 
from backend.api import (
    receiver_router,
    retrieve_router,
    insert_router,
    compare_router,
)
from backend.config import config

if config.deploy_env != "production":
    logging.basicConfig(level=logging.DEBUG)

# 
# ここにAPIのエンドポイントとなるファイルを追加していく
# 
app = FastAPI()
app.include_router(receiver_router)
app.include_router(insert_router)
app.include_router(retrieve_router)
app.include_router(compare_router)


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
"""
ここまで
"""


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
