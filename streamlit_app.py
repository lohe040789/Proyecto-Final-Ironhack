import streamlit as st
import pandas as pd
#sidebar
st.sidebar.title('Creado por ...')
st.title('Proyecto Final') 
st.title('Hagamos tu Menu')


st.header('Necesitamos unos datos para poder ayudarte')
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")



# Parametros de entrada:

Genero = st.sidebar.selectbox('Genero?',('Hombre', 'Mujer'))
Edad = st.sidebar.slider('Que edad tienes?', 0, 130, 25)
Peso = st.sidebar.slider('Cuanto pesas?', 0, 130, 25)
Estatura = st.sidebar.slider('Cuanto mides en "cm"?', 0, 130, 25)
Objetivo = st.sidebar.selectbox('Que objetivo tienes?', ('Perder peso', 'Ganar masa muscular', 'Mantenerse'))
Horario_de_la_actividad = st.sidebar.selectbox('A que hora realizas actividad fisica?', ('Mañana', 'Tarde', 'Noche'))
Tipo_de_actividad = st.sidebar.selectbox('Que tipo de actividad realizas?', ('Sedentario', 'Ligera', 'Moderada', 'Intensa'))
Tiempo_de_actividad = st.sidebar.slider('Cuantas horas al dia realizas actividad fisica?', 0, 4, 1)