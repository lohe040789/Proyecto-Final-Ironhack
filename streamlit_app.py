import streamlit as st
import pandas as pd
#sidebar
st.sidebar.title('Creado por ...')
st.title('Prueba de Streamlit') 
age = st.slider('How old are you?', 0, 130, 25)