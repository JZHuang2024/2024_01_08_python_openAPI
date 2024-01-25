#2023.01.24.wed.PM04:22一次可以傳5筆資料

#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#這個練習必須在虛擬主機下進行,因為安裝了需要的模組在這虛擬主機下openAPI 專案下. 在Git Bash終端機下(python3.10.8)下
#       起初是在    JZ@WINDOWS-QET06QS MINGW64 ~/Documents/GitHub/2024_01_08_python_openAPI(main)下
#       先執行指令: cd openAPI
#       變成        JZ@WINDOWS-QET06QS MINGW64 ~/Documents/GitHub/2024_01_08_python_openAPI/openAPI (main)下
#       指令: source .venv/scripts/activate    ➤➤➤➤進入虛擬主機 .venv  
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
#
#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#此main5.py必須通過以下指令啟動 server
#
#   FastAPI 使用Uvicorn 作為其預設的Web 伺服器，
#   是因為Uvicorn 是一個非常快速、可靠且易於使用的ASGI 伺服器，可以在處理大量並發連接時保持穩定和高效。
#
#   main: 代表的是 main.py 這個檔案
#   app: 是 main.py 中創建的 FastAPI 實例
#   --reload: 當程式碼改變時 server 會自動重啟，只會於開發時使用
#
#   (https://ithelp.ithome.com.tw/articles/10290597)
#
#指令:uvicorn main5:app --reload   (非按右上角 " ▷ " 執行)
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲


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


#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#2023.01.24.wed.AM11:30將資料傳到redis並開啟RedisInsight查看資料
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

    date_get = redis_conn.lrange('pico_w:date',-1,-1)[0].decode()
    address_get = redis_conn.hget('pico_w:address',date_get).decode()
    temperature_get = redis_conn.hget('pico_w:temperature',date_get).decode()
    light_get = redis_conn.hget('pico_w:light',date_get).decode()
    print(date_get)
    print(address_get)
    print(temperature_get)
    print(light_get)
 #▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
    return {"狀態":"儲存成功"}

@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float=0.0):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    return {"狀態":"儲存成功"}

'''
#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼2023.01.24.wed.PM03:55多一個節點▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
@app.get("/pico_w/")
async def read_item(count:int=1):
    date_get = redis_conn.lrange('pico_w:date',-1,-1)[0].decode()
    address_get = redis_conn.hget('pico_w:address',date_get).decode()
    temperature_get = redis_conn.hget('pico_w:temperature',date_get).decode()
    light_get = redis_conn.hget('pico_w:light',date_get).decode()
    print(date_get)
    print(address_get)
    print(temperature_get)
    print(light_get)
    return {'date':date_get,
            'address':address_get,
            'temperature':temperature_get,
            'light':light_get
            }
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲2023.01.24.wed.PM03:55多一個節點▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
'''


#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#2023_01_24_Wed_PM04:22一次可以傳5筆資料
class Pico_w(BaseModel):
    date:str
    address:str
    temperature:float
    light:float

@app.get("/pico_w/")
async def read_item(count:int=1):
    date_list = redis_conn.lrange('pico_w:date',-count,-1)
    dates = [date.decode() for date in date_list]
    all_Data:[Pico_w] = []
    for date in dates:
        address_get = redis_conn.hget('pico_w:address',date).decode()
        temperature_get = redis_conn.hget('pico_w:temperature',date).decode()
        light_get = redis_conn.hget('pico_w:light',date).decode()
        item = Pico_w(date=date,address=address_get,temperature=float(temperature_get),light=float(light_get))
        all_Data.append(item)

    
    return all_Data

#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲











#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
#1.進入Thunder Client 在上方按下 New Request
#  輸入 http://127.0.0.1:8000/pico_w/2024-01-24 11:36?address=chicken_KFC&celsius=26.6789&light=45987&temperature=27.5
#  按下 SEND 若成功右邊視窗出現
#            
#            {
#             "狀態": "儲存成功"
#            }
#
#  VScode 若成功下方終端機會出現
#        INFO:     Application startup complete.
#        日期:2024-01-24 11:36
#        位置:chicken_KFC
#        攝氏:26.6789
#        光線:45987.0
#        INFO:     127.0.0.1:5554 - "GET /pico_w/2024-01-24%2011%3A36?address=chicken_KFC&celsius=26.6789&light=45987&temperature=27.5 HTTP/1.1" 200 OK 2024-01-24 11:36
#
#  第1(2024-01-24 11:36)組資料成功傳入render server 開啟RedisInsight查看第1組資料
#
#                                                    ▼
#2.接輸入 http://127.0.0.1:8000/pico_w/2024-01-24 11:37?address=chicken_KFC&celsius=26.6789&light=45987&temperature=27.5
#  按下 SEND 若成功出現下方
#            
#            {
#             "狀態": "儲存成功"
#            }
#  下方伺服器成功會出現
#        INFO:     Application startup complete.
#        日期:2024-01-24 11:37
#        位置:chicken_KFC
#        攝氏:26.6789
#        光線:45987.0
#        INFO:     127.0.0.1:5554 - "GET /pico_w/2024-01-24%2011%3A36?address=chicken_KFC&celsius=26.6789&light=45987&temperature=27.5 HTTP/1.1" 200 OK 2024-01-24 11:37
#
#  第2(2024-01-24 11:37)組資料成功傳入render server 開啟RedisInsight查看第2組資料
#
#                                                    ▼
#3.接輸入 http://127.0.0.1:8000/pico_w/2024-01-24 11:37?address=chicken_KFC&celsius=26.6789&light=45987&temperature=27.5
#  按下 SEND 若成功出現下方
#            
#            {
#             "狀態": "儲存成功"
#            }
#  下方伺服器成功會出現
#        INFO:     Application startup complete.
#        日期:2024-01-24 11:37
#        位置:chicken_KFC
#        攝氏:26.6789
#        光線:45987.0
#        INFO:     127.0.0.1:5554 - "GET /pico_w/2024-01-24%2011%3A36?address=chicken_KFC&celsius=26.6789&light=45987&temperature=27.5 HTTP/1.1" 200 OK 2024-01-24 11:37
#
#  第3(2024-01-24 11:37)組資料成功傳入render server 開啟RedisInsight查看第3組資料