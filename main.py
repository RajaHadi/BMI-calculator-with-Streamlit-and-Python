import streamlit as st
import pandas as pd

st.title("BMI  Calculator")

height= st.slider("Enter your Height (cm)", 100, 250, 170)
weight= st.slider("Enter your Weight (kg)", 40, 200, 70)
bmi= weight / ((height/100)**2)
st.write(f"Your BMI is:{bmi:.2f} ")
st.write("BMI Categories")
st.write("Underweight: less than 18.5")
st.write("Normal weight: between 18.5 and 24.9")
st.write("Overweight: between 25 and 29.9")
st.write("Obesity: 30 or greater")
