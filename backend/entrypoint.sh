#!/bin/sh

# # UDPレシーバーを実行
# python mcp_receiver/main.py &

# FastAPIアプリケーションをバックグラウンドで起動この　”＆”　が重要
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload 

# すべてのバックグラウンドプロセスが終了するまで待機
wait
