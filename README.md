![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Proyecto Final 
## Ironhack
### Data Analytics 

## Recomendador de Recetas

Como proyecto final realice un recomendador de recetas ayudar a los usuarios a encontrar recetas que se adapten a sus preferencia y parámetros de vida, donde tomamos en cuenta datos como peso, estatura y edad para hacer un cálculo de gasto energético y que tipo de actividad realizan para especificar el consumo diario de calorías por día.

## Obtención de los datos, limpieza y carga.

La obtención de datos fue a través de la API `EDAMAM` donde necesitamos obtener la clave de la API, asi poder acceder a los datos de recetas y comenzar hacer solicitudes 
La respuesta de Edamam es un archivo JSON con información sobre las recetas. Ejecute un código (`
extraccion_api.ipynb`)para que luego itere sobre cada receta en la respuesta de la API y extrae información nutricional y otros detalles de la receta.
 Luego, crea un diccionario con estos datos y los agregue a la lista, para llevarlos a un DataFrame de Pandas Para luego cargarlos a una base de datos MySQL y poder hacer consulta sobre cada receta.

## Visualización con Streamlit

Cree una pequeña versión del recomendador por Stremlit (`streamlit_app.py`) en donde manualmente introduces tus datos y actividad física. Calcula la cantidad de calorías según un objetivo y por siguiente calculas las recetas que se ajustan a ese objetivo. Dando como resultado una imagen de la receta, la cantidad de calorías , una URL donde puedes seguir los pasos de la receta y un gráfico de Tarta para ver la distribución de proteínas , carbohidratos y grasas de la misma.
