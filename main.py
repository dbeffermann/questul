import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")

df = pd.read_excel("consolidado.xlsx", engine='openpyxl').drop(columns = "Unnamed: 0")

# Selector de preguntas.
pregunta = st.selectbox(f"Preguntas: {df.shape[0]}", df.question)
question = df[df['question'] == pregunta].iloc[0]

# Formulario de pregunta.
with st.form("my_form"):
    st.header(question.question)

    a = st.checkbox(label = question.a, key = "a")
    b = st.checkbox(label = question.b, key = "b")
    c = st.checkbox(label = question.c, key = "c")
    d = st.checkbox(label = question.d, key = "d")
    e = st.checkbox(label = question.e, key = "e")
    f = st.checkbox(label = question.e, key = "f")
    submit = st.form_submit_button("Submit")

if submit:
    st.write(a,b,c,d,e,f)

import timer
timer.timer()
