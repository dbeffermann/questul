import time
import streamlit as st

# Timer.
def timer(segundos=120):

    cuenta = st.empty()

    for secs in range(segundos,0,-1):
        mm, ss = secs//60, secs%60
        cuenta.metric("Tiempo", f"{mm:02d}:{ss:02d}")
        time.sleep(1)