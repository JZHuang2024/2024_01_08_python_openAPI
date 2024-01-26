#2024_01_24_AM11:59

#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#此main.py必須在虛擬主機執行.指令:uvicorn main:app --reload
#非按右上角 " ▷ " 執行
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
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
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def get_item(item_id:int):
    print(f"使用者輸入了:{item_id}")
    return {"item_id":item_id}

@app.get("/items/{date}/{celsius}")
async def get_item(date:str,celsius:float):
    print(f"日期:{date}")
    print(f"溫度:{celsius}")
    return {"日期":date,"攝氏溫度":celsius}



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


#2023.01.24.wed.AM11:30

@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    print(f"光線:{light}")    #加入光線
    return {"狀態":"儲存成功"}

@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float=0.0):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    return {"狀態":"儲存成功"}

#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#此main2.py必須在虛擬主機執行.指令:uvicorn mainXXXX:app --reload (mainXXXX是測試檔)
#非按右上角 " ▷ " 執行
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
#1.然後,進瀏覽器執行http://127.0.0.1:8000/docs
#2.也可安裝 Thunder Client在Visual Studio Code進行無腳本測試
#    Thunder Client 是用於 Visual Studio Code 的輕量級 Rest API 客戶端擴展，具有簡單易用的 UI。
#    支持集合和環境變數和 GraphQL 查詢，以及使用基於 GUI 的界面進行無腳本測試。
#    所有請求的資料都本地保存在您的設備上。
#3.進入Thunder Client 在上方按下 New Request
#    GET處輸入http://127.0.0.1:8000/pico_w/2024-01-24 11:36?2024-01-24 11:36? 
#                                                                            ▲▲▲▲▲▲後面這段在Thunder Client下面輸入▲▲▲▲▲▲▲▲▲▲
#    在下方輸入address     chicken_KFC
#             celsius     26.6789
#             light       45987
#  或直接輸入 http://127.0.0.1:8000/pico_w/2024-01-24 11:36?address=chicken_KFC&celsius=26.6789&light=45987
#                                                                           
#  按下 SEND 若成功出現下方
#            
#            {
#             "狀態": "儲存成功"
#            }
#4. 下方伺服器成功會出現
#        INFO:     Application startup complete.
#        日期:2024-01-24 11:36
#        位置:chicken_KFC
#        攝氏:26.6789
#        光線:45987.0
#        INFO:     127.0.0.1:3986 - "GET /pico_w/2024-01-24%2011%3A36?address=chicken_KFC&celsius=26.6789&light=45987 HTTP/1.1" 200 OK
#
#5. 下個步驟 修改C:\Users\user\Documents\GitHub\2024_01_08_python_openAPI\pico_w\lesson11_1_08.py
#
#
#
#
#
