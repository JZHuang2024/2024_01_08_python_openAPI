#2024_01_26_AM1110整合lesson12.ipynb 兩段程式
#必須在終端機下的命令列執行 指令: python main.py
import requests
import pandas as pd

url = 'https://openapi-test-6vnu.onrender.com/pico_w/?count=5'

r = requests.get(url=url)

if r.status_code == 200:
    print("下載成功")
    data = r.json()

dataFrame = pd.DataFrame(data)
print(dataFrame)