#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#此main.py必須在虛擬主機執行.指令:uvicorn main:app --reload
#非按右上角 " ▷ " 執行
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
#
#ASGI是非同步伺服器閘道介面（Asynchronous Server Gateway Interface）的縮寫，
#   是Python非同步Web框架Django、FastAPI等的新的伺服器介面規格。
#
#from…import：導入了一個模組中的一個函數；註：相當於導入的是一個資料夾中的文件，是個絕對路徑。
#
#什麼是 Uvicorn？ ◀◀◀◀這個模組在 requirements.txt中有先安裝給虛擬主機了
#   uvicorn 是一個輕量級高效的web伺服器框架。 Uvicorn 是基於 uvloop 和 httptools 構建的非常快速的 ASGI 伺服器。
#
#什麼是 FastAPI？ ◀◀◀◀這個模組在 requirements.txt中有先安裝給虛擬主機了
#   FastAPI是在Python中構建RESTful API的現代Web框架
#
#什麼是 python-dotenv？ ◀◀◀◀這個模組在 requirements.txt中有先安裝給虛擬主機了
#   python-dotenv 模組 : 處理帳號、密碼及金鑰…等敏感資訊的存放問題
#   (請參考說明https://kirin.idv.tw/python-dotenv-sensitive-secret-data-storage/)
#
##什麼是 os？ ◀◀◀◀這個Python 的標準函式 ❌❌❌requirements.txt❌❌❌不需要安裝
#
#ping localhost 有什麼用？ 
#       例如，您可以輕鬆開啟命令提示字元或終端機並輸入「ping localhost」或“ping 127.0.0.1”。
#       本機測試將顯示一切的執行情況，從接收、傳送或遺失的資料包數量，到資料傳輸所需的時間。
#       Python 的標準函式「os」提供了操作系統中檔案的方法，可以針對檔案進行重新命名、編輯、刪除等相關操作
#
#
#import 模組：導入模組；註：相當於導入的是資料夾，是相對路徑。

#
#
#
#os.environ
#       在python 中，透過 os.environ 取得環境變數。什麼是環境變數呢？ 環境變數是程式和作業系統之間的通訊方式。 
#       有些字元不宜明文寫進程式碼裡，例如資料庫密碼，個人帳戶密碼，如果寫進自己本機的環境變數裡，
#       程式用的時候透過 os.environ.get() 取出就行了。 這樣開發人員本機測試的時候用的是自己本機的一套密碼，
#       生產環境部署的時候，用的是公司的公共帳號和密碼，這樣就能增加安全性。 os.environ 是一個字典，是環境變數的字典。 
#       透過os.environ.get(“HOME”)，就可以取得環境變數HOME的值，如果有這個鍵，回傳對應的值；如果沒有，傳回 none





#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#此main.py必須在虛擬主機執行.指令:uvicorn main:app --reload
#非按右上角 " ▷ " 執行
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
'''
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


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q:str | None = None):
#    return {"item_id": item_id, "q": q}
#(2024.01.22.Monday.AM11:55 modify)



#2024.01.22.Monday.AM11:55
@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float=0.0):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    return {"狀態":"儲存成功"}
'''


'''
#2024_01_24_AM11:59
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


@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    print(f"光線:{light}")
    return {"狀態":"儲存成功"}
'''

#2024_01_24_PM03:30
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


@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):
    #print(f"日期:{date}")
    redis_conn.rpush('pico_w:date',date)
    #print(f"位置:{address}")
    redis_conn.hset('pico_w:address',mapping={date:address})
    #print(f"攝氏:{celsius}")
    redis_conn.hset('pico_w:temperature',mapping={date:celsius})
    #print(f"光線:{light}")
    redis_conn.hset('pico_w:light',mapping={date:light})
    return {"狀態":"儲存成功"}

#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#此main.py必須在虛擬主機執行.指令:uvicorn main:app --reload
#非按右上角 " ▷ " 執行
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲