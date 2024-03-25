import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title("Streamlit入門")

st.write("プログレスバー表示")
"Start！"

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!"
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write("ここは右のカラム")


ex = st.expander("問い合わせ")
ex.write("問い合わせ内容を書く")
# text=st.text_input("あなたの趣味を教えてください")
# condition=st.slider("あなたの調子は？",0,100,50)

#チェックボックスで画像の可否をつくる
# if st.checkbox("Show Img"):
#     img=Image.open("vvv.jpg")
#     st.image(img,caption="kawaii",use_column_width=True)

# #セレクトボックス
# option=st.selectbox("あなたが好きな数字を教えてください",list(range(1,11)))

# "あなたの好きな数字は、",option,"です"


# "あなたの好きな趣味は、",text,"です"


# "あなたの調子は、",condition,"です"