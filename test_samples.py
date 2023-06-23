import streamlit as st

st.header("st.selectbox")

option = st.selectbox(
  "What is your favourite color?, ("Blue", "Red", "Green"))

st.write("your favourite colir is ", option)
