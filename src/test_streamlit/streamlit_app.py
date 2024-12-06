import streamlit as st
import pandas as pd
st.title('Hello, Streamlit!')
st.write('これは最初のStreamlitアプリケーションです。')

df = pd.DataFrame(
    {
        "名前":['Alice', 'Bob', 'Charlie'],
        'スコア': [85, 90, 78]
    }
)

st.write("学生のスコア")
st.dataframe(df)