#2024_01_26_AM1110整合lesson12.ipynb 兩段程式
#必須在終端機下的命令列執行 指令: python main.py
'''
import requests
import pandas as pd

url = 'https://openapi-test-6vnu.onrender.com/pico_w/?count=5'

r = requests.get(url=url)

if r.status_code == 200:
    print("下載成功")
    data = r.json()

dataFrame = pd.DataFrame(data)
print(dataFrame)
'''

#2024_01_26_AM1145 讓資料在網頁開啟
#streamlit指令參考  https://streamlit.io/
#必須在終端機下的命令列執行 指令: streamlit run main.py
'''
import requests
import pandas as pd
import streamlit as st

url = 'https://openapi-test-6vnu.onrender.com/pico_w/?count=5'

r = requests.get(url=url)

if r.status_code == 200:
    print("下載成功")
    data = r.json()

dataFrame = pd.DataFrame(data)

st.header("學院養雞場")
st.divider()
st.caption("溫度-光線表表😍")
st.write(dataFrame)
st.divider()
st.caption("光線")
st.line_chart(dataFrame,x='date',y='light')
st.divider()
st.caption("溫度")
st.line_chart(dataFrame,x='date',y='temperature',color='#ff0000')
'''


#2024_01_26_AM1145 讓資料在網頁每10秒更新一次
#requirements.txt 必須加入安裝 streamlit-autorefresh
#第1次必須在終端機下的命令列執行streamlit-autorefresh安裝 指令: pip install -r requirements.txt
#必須在終端機下的命令列執行 指令: streamlit run main.py


import requests
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

url = 'https://openapi-test-6vnu.onrender.com/pico_w/?count=10'
#自動reload頁面每10秒
st_autorefresh(interval=10000, limit=100, key="fizzbuzzcounter")

r = requests.get(url=url)

if r.status_code == 200:
    print("下載成功")
    data = r.json()

dataFrame = pd.DataFrame(data)

st.header("學院養雞場")
st.divider()
st.caption("溫度-光線表表😍")
st.write(dataFrame)
st.divider()
st.caption("光線")
st.line_chart(dataFrame,x='date',y='light')
st.divider()
st.caption("溫度")
st.line_chart(dataFrame,x='date',y='temperature',color='#ff0000')

