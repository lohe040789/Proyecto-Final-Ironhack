import streamlit as st
import pandas as pd

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
        actividad_nivel = (20 * GEB_resultado /100) + GEB_resultado
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

def main():
    st.sidebar.title('Creado por "Lohe"')
    st.title('Proyecto Final') 
    st.title('Hagamos tu Menu')
    st.header('Necesitamos unos datos para poder ayudarte')

    # Parametros de entrada:
    Genero = st.sidebar.selectbox('Genero?',('Hombre', 'Mujer'))
    Tipo_de_actividad = st.sidebar.selectbox('Que tipo de actividad realizas?', ('Sedentario', 'Ligera', 'Moderada', 'Intensa'))
    Objetivo = st.sidebar.selectbox('Que objetivo tienes?', ('Perder peso', 'Ganar masa muscular', 'Mantenerse'))
    Horario_de_la_actividad = st.sidebar.selectbox('A que hora realizas actividad fisica?', ('Mañana', 'Tarde', 'Noche'))
    Edad = st.sidebar.slider('Que edad tienes?', 10, 85, 25)
    Peso = st.sidebar.slider('Cuanto pesas?', 30, 150, 25)
    Estatura = st.sidebar.slider('Cuanto mides en "cm"?', 100, 200, 150)
    Tiempo_de_actividad = st.sidebar.slider('Cuantas horas al dia realizas actividad fisica?', 0, 4, 1)

    # Botón para calcular
    if st.button('Calcular'):
        # Ejecuta la función con los parámetros introducidos
        resultado = calcular_kcal(Genero, Tipo_de_actividad, Objetivo, Horario_de_la_actividad, Edad, Peso, Estatura, Tiempo_de_actividad)
        # Muestra el resultado
        st.metric(label='Kcal', value=resultado)

if __name__ == '__main__':
    main()

#En el teminal: streamlit run streamlit_app.py