import streamlit as st

st.header("st.multiselect")

options = st.multiselect(
  "What are your favourite colors", ["Yellow", "Red", "Orange", "Blue"]
)

st.write("My favourites colors are: ",options)
