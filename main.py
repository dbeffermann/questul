import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

df = pd.read_excel("consolidado.xlsx", engine='openpyxl').drop(columns = "Unnamed: 0")

# Selector de preguntas.
pregunta = st.selectbox(f"Preguntas: {df.shape[0]}", df.question)
question = df[df['question'] == pregunta].iloc[0]
#indice , question = question.index, question.iloc[0]

# Formulario de pregunta.
with st.form("my_form"):
    st.header(question.question)

    a = st.checkbox(label = question.a.replace("(Correct)", ""), key = "a")
    b = st.checkbox(label = question.b.replace("(Correct)", ""), key = "b")
    c = st.checkbox(label = question.c.replace("(Correct)", ""), key = "c")
    d = st.checkbox(label = question.d.replace("(Correct)", ""), key = "d")
    e = st.checkbox(label = question.e.replace("(Correct)", ""), key = "e")
    f = st.checkbox(label = question.e.replace("(Correct)", ""), key = "f")
    submit = st.form_submit_button("Submit")

# Botones Anterior y Siguiente.
#col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns([.5,.5,1,1,1,1,1,1,1,1,1,1])
#anterior = col1.button("Anterior")
#siguiente = col2.button("Siguiente")

#if siguiente:
   #question = df.iloc[int(indice[0])+1]

# Verificar respuesta.
if submit:

    correctas = [True if "(Correct)" in i else False for i in question["a":"f"]]
    respuesta = [a,b,c,d,e,f]
    resultado = correctas == respuesta

    if resultado == True:
        st.success('Correcto!', icon="🚀")
        st.balloons()
    else:
        st.error('Incorrecto: Intentalo de nuevo', icon="🚨")

    #st.code(question.explicacion)
    tab1, tab2 = st.tabs(["Opción correcta", "Opciones incorrectas"])
    tab1.write(question.explicacion[question.explicacion.find("Opción correcta:"):question.explicacion.find("Opciones incorrectas:")])
    tab2.write(question.explicacion[question.explicacion.find("Opciones incorrectas:"):])
# Timer.
import timer
segundos = st.sidebar.slider("Segundos por pregunta:", 10, 120, 120, 10)
timer.timer(segundos)
