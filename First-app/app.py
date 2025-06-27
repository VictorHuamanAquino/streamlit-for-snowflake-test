import pandas as pd
import streamlit as st

st.title("Hierarchical Data Viewer")

st.header("This is a header")
st.subheader("subheader")
st.caption("caption")

st.write("This is example of 'write' : Code of df")
st.code("df = pd.read_csv('data/employees.csv',header = 0)\nst.dataframe(df)","python")

df = pd.read_csv("data/employees.csv",header = 0)
st.dataframe(df)


edges = ""

for _,row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'

st.divider()

d = f'digraph {{\n{edges}}}'
st.graphviz_chart(d)

st.divider()
st.latex("...")
st.error("this is an error")
st.info("this is info")
st.warning("this is warning")
st.success("this is success")


