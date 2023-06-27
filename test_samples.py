import streamlit as st

st.header("st.checkbox")

st.write("Select your favourite color:")

blue = st.checkbox("blue")
red = st.checkbox("red")
green = st.checkbox("green")

if blue:
  st.write("Your favourite color is blue 🔵")
if red:
  st.write("Your favourite color is red 🔴")
if green:
  st.write("Your favourite color is green 🟢")
