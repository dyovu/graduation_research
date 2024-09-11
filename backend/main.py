"""
ここから変更した新しいコード
"""
import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 
# ここにAPIのエンドポイントとなるファイルを追加していく
# 
from backend.api import (
    insertion_router,

)
from backend.config import config

if config.deploy_env != "production":
    logging.basicConfig(level=logging.DEBUG)

# 
# ここにAPIのエンドポイントとなるファイルを追加していく
# 
app = FastAPI()
app.include_router(insertion_router)
app.include_router()


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
