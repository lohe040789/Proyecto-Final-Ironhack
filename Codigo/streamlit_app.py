import streamlit as st
import pandas as pd
import numpy as np
import sqlalchemy as sa
import plotly.graph_objs as go
from PIL import Image
from io import BytesIO


st.sidebar.title('Rellena tus datos')
    # Parametros de entrada:
Genero = st.sidebar.selectbox('Genero?',('Hombre', 'Mujer'))
Tipo_de_actividad = st.sidebar.selectbox('Que tipo de actividad realizas?', ('Sedentario', 'Ligera', 'Moderada', 'Intensa'))
Objetivo = st.sidebar.selectbox('Que objetivo tienes?', ('Perder peso', 'Ganar masa muscular', 'Mantenerse'))
Horario_de_la_actividad = st.sidebar.selectbox('A que hora realizas actividad fisica?', ('Mañana', 'Tarde', 'Noche'))
Edad = st.sidebar.slider('Que edad tienes?', 10, 85, 25)
Peso = st.sidebar.slider('Cuanto pesas?', 30, 150, 25)
Estatura = st.sidebar.slider('Cuanto mides en "cm"?', 100, 200, 150)
Tiempo_de_actividad = st.sidebar.slider('Cuantas horas al dia realizas actividad fisica?', 0, 4, 1)

# Función para calcular el consumo diario de calorías
def calcular_kcal(Genero, Tipo_de_actividad, Objetivo, Horario_de_la_actividad, Edad, Peso, Estatura, Tiempo_de_actividad):
    # Aquí va todo el código para calcular el consumo diario de calorías
    edad = Edad
    genero = Genero.lower()
    peso = Peso
    estatura = Estatura
    if genero == 'hombre':
        n1 = 66.5
        p = 13.75 * peso
        at = 5.003 * estatura
        e = 6.77 * edad
    elif genero == 'mujer':
        n1 = 655.1
        p = 9.56 * peso
        at = 1.85 * estatura
        e = 4.68 * edad

    #GEB mujer= 665.1 + (9.56 x p) + (1.85 x cm) – (4.7 x años) + actividad
    #GEB hombre = 66.5 + (13.75 x p) + (5.003 x cm) - (6.77 x años) + actividad
    GEB_resultado = n1 + at + p - e

    actividad_nivel = Tipo_de_actividad.lower()

    if actividad_nivel == 'sedentario':
        actividad_nivel = (5 * GEB_resultado /100) + GEB_resultado
    elif actividad_nivel == 'ligera':
        actividad_nivel = (50 * GEB_resultado /100) + GEB_resultado
    elif actividad_nivel == 'moderada':
        actividad_nivel = (75 * GEB_resultado /100) + GEB_resultado
    elif actividad_nivel == 'intensa':
        actividad_nivel = (100 * GEB_resultado /100) + GEB_resultado

# Lo mas saludable a la hora de perder o ganar peso, se recomienda que sean 500kcal por dia. 
    objetivo = Objetivo.lower()
    if objetivo == 'perder peso':
        kcal = actividad_nivel - 500
    elif objetivo == 'mantenerse':
        kcal = actividad_nivel
    elif objetivo == 'ganar masa muscular':
        kcal = actividad_nivel + 500     

        # return el resultado
    return kcal


st.title('Proyecto Final') 
st.title('Hagamos tu Menu')
st.header('Necesitamos unos datos para poder ayudarte')


    # Botón para calcular
if st.button('Calcular'):
        # Ejecuta la función con los parámetros introducidos
    resultado = calcular_kcal(Genero, Tipo_de_actividad, Objetivo, Horario_de_la_actividad, Edad, Peso, Estatura, Tiempo_de_actividad)
    resultado = int(resultado)
        # Muestra el resultado
    st.metric(label='Kcal', value=resultado)

# Función para consultar las recetas

def consulta_recetas():
    # Conectar a la base de datos utilizando sqlalchemy
    str_conn = 'mysql+pymysql://root:Reina-0601@localhost:3306/recetas'
    engine = sa.create_engine(str_conn)

    # Obtener una conexión a la base de datos
    conn = engine.connect()

    # Consultar las 5 recetas que sumen cierta cantidad de calorías
    calorias_objetivo = calcular_kcal(Genero, Tipo_de_actividad, Objetivo, Horario_de_la_actividad, Edad, Peso, Estatura, Tiempo_de_actividad)
    calorias_objetivo = int(calorias_objetivo)
    print(calorias_objetivo)
    query = sa.text(f"SELECT Nombre, Calorías_por_porción, Proteínas_por_porción, Carbohidratos_por_porción, Grasas_por_porción, URL,Imagen, Tipo_de_comida FROM recetas WHERE Calorías_por_porción <= {calorias_objetivo} AND Tipo_de_comida IN ('breakfast', 'lunch', 'dinner', 'snack') ORDER BY RAND() LIMIT 5")
    
    result = conn.execute(query)

    # Mostrar los resultados en Streamlit
    st.write(f"Mostrando las 5 recetas que suman {calorias_objetivo} calorías:")
    for nombre, calorias, proteinas, carbohidratos, grasas, URL ,imagen_url, Tipo_de_comida  in result:
        st.write(f"- {nombre}: {calorias} calorías")
        st.write(f" Preparación: {URL} ")
        st.write(f" Tipo de comida: {Tipo_de_comida} ")

        # Mostrar la imagen de la receta
        st.image(imagen_url, use_column_width=True,
                 caption=f"Imagen de {nombre}",#tamaño de la imagen en la pagina web 
                 clamp=True, channels='RGB', output_format='auto')
        
        # Crear un gráfico de tarta
        labels = ['Proteínas', 'Carbohidratos', 'Grasas']
        values = [proteinas, carbohidratos, grasas]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        st.plotly_chart(fig)


    # Cerrar la conexión a la base de datos
    conn.close()

    # Crear un botón en Streamlit que llame a la función cuando se presiona
if st.button("Consultar recetas"):
    consulta_recetas()



#En el teminal: streamlit run streamlit_app.py