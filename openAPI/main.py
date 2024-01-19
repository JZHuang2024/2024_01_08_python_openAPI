#ASGI是非同步伺服器閘道介面（Asynchronous Server Gateway Interface）的縮寫，
#   是Python非同步Web框架Django、FastAPI等的新的伺服器介面規格。
#
#什麼是 Uvicorn？ ◀◀◀◀這個模組在 requirements.txt中有先安裝給虛擬主機了
#   uvicorn 是一個輕量級高效的web伺服器框架。 Uvicorn 是基於 uvloop 和 httptools 構建的非常快速的 ASGI 伺服器。
#
#什麼是 FastAPI？ ◀◀◀◀這個模組在 requirements.txt中有先安裝給虛擬主機了
#   FastAPI是在Python中構建RESTful API的現代Web框架
#
#
#什麼是 python-dotenv？ ◀◀◀◀這個模組在 requirements.txt中有先安裝給虛擬主機了
#   python-dotenv 模組 : 處理帳號、密碼及金鑰…等敏感資訊的存放問題
#   (請參考說明https://kirin.idv.tw/python-dotenv-sensitive-secret-data-storage/)
#
#
##什麼是 os？ ◀◀◀◀這個Python 的標準函式 ❌❌❌requirements.txt❌❌❌不需要安裝
#
#ping localhost 有什麼用？ 
#       例如，您可以輕鬆開啟命令提示字元或終端機並輸入「ping localhost」或“ping 127.0.0.1”。
#       本機測試將顯示一切的執行情況，從接收、傳送或遺失的資料包數量，到資料傳輸所需的時間。
#
#
#
#import 模組：導入模組；註：相當於導入的是資料夾，是相對路徑。
#from…import：導入了一個模組中的一個函數；註：相當於導入的是一個資料夾中的文件，是個絕對路徑。
#Python 的標準函式「os」提供了操作系統中檔案的方法，可以針對檔案進行重新命名、編輯、刪除等相關操作






from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()


@app.get("/")
def read_root():
    counter = redis_conn.incr('test:increment',1)
    return {"Counter": counter}

@app.get("/counter/{c}")
def counter(c:int):
    counter = redis_conn.incr('test:increment',c)
    return {"Counter": counter}


@app.get("/items/{item_id}")
def read_item(item_id: int, q:str | None = None):
    return {"item_id": item_id, "q": q}