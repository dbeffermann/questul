import streamlit as st
import pandas as pd
import time

# Configuración de la página
st.set_page_config(
    page_title='Aplicación de Evaluación en Línea',
    page_icon='logo.png',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# Cargar datos de preguntas
@st.cache_data
def leer_df(archivo="consolidado.xlsx"):
    df = pd.read_excel(archivo, engine='openpyxl').drop(columns="Unnamed: 0")
    return df

preguntas = leer_df()

# Diseño del encabezado
st.sidebar.image('logo.png')

col1, col2 = st.columns(2)

if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}
if 'n_actual' not in st.session_state:
    st.session_state.n_actual = 0
if 'status' not in st.session_state:
    st.session_state.status = 'on'

def siguiente():
    st.session_state.n_actual += 1

def guardar_respuestas_en_cache(question_, a_, b_, c_, d_, e_, f_):
    st.session_state.respuestas.update({question_: [a_, b_, c_, d_, e_, f_]})

question = preguntas.iloc[st.session_state.n_actual]
st.header(question.question)
st.write(['Correct' in i for i in question.values.tolist()])

with st.form("my_form", clear_on_submit=True):
    a = st.checkbox(label=question.a.replace("(Correct)", ""), key="a")
    b = st.checkbox(label=question.b.replace("(Correct)", ""), key="b")
    c = st.checkbox(label=question.c.replace("(Correct)", ""), key="c")
    d = st.checkbox(label=question.d.replace("(Correct)", ""), key="d")
    e = st.checkbox(label=question.e.replace("(Correct)", ""), key="e")
    f = st.checkbox(label=question.f.replace("(Correct)", ""), key="f")
    submit_btn = st.form_submit_button("Enviar Respuestas")

if submit_btn:
    st.write([a,b,c,d,e,f])
    guardar_respuestas_en_cache(question.question, a, b, c, d, e, f)
    siguiente()
    st.experimental_rerun()

def terminar_sesion():
    df_out = pd.DataFrame(st.session_state.respuestas).T.reset_index()
    df_out.columns = ['Pregunta', 'a', 'b', 'c', 'd', 'e', 'f']
    st.header("Resultados")
    st.dataframe(df_out)
    df_out.to_csv("reporte.csv", sep=';', index=False)
    st.session_state.status = 'end'

if len(st.session_state.respuestas) > 0:
    terminar = st.button("Terminar Test")
    if terminar:
        terminar_sesion()

# Pie de página con derechos reservados
st.markdown("---")
st.markdown("&copy; 2023 Todos los derechos reservados - Aplicación de Evaluación en Línea")
