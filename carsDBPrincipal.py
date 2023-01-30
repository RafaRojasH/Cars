import streamlit as st
import pandas as pd
from PIL import Image

data = pd.read_csv('carsDB.csv')
df = pd.DataFrame(data, columns=['Nombre', 'Version', 'Pelicula', 'Tipo', 'Observaciones', 'Imagen'])

def open_image(image):
    st.image(image, width=300)


st.title('Cars de Rafa')

opcion = st.sidebar.radio('Opción para buscar: ',
                          ('Nombre', 'Pelicula', 'Tipo'))


if opcion == 'Nombre':
    nombres = df['Nombre'].drop_duplicates()
    nombre = st.sidebar.selectbox('Elige un nombre', nombres)
    versiones = df['Version'].loc[df['Nombre'] == nombre]
    vers = pd.Series(['Todos'])
    vers = vers.append(versiones)
    version = st.sidebar.selectbox('Elige una versión', vers)
    imagen = []
    if version != 'Todos':
        for i in df.index:
            if df['Nombre'][i] == nombre and df['Version'][i] == version:
                imagen.append('Imagenes/' + df['Imagen'][i] + '.jpg')
        for image in imagen:
            button_image = st.button('Open image')
            if button_image:
                open_image(imagen)
        st.image(imagen, width=300, use_column_width=True)
    else:
        for i in df.index:
            if df['Nombre'][i] == nombre:
                imagen.append('Imagenes/' + df['Imagen'][i] + '.jpg')
        for image in imagen:
            button_image = st.button('Open image')
            if button_image:
                open_image(imagen)
        st.image(imagen, width=300, use_column_width=True)
elif opcion == 'Pelicula':
    peliculas = df['Pelicula'].drop_duplicates()
    pelicula = st.sidebar.selectbox('Elige una película', peliculas)
    imagen = []
    for i in df.index:
        if df['Pelicula'][i] == pelicula:
            imagen.append('Imagenes/' + df['Imagen'][i] + '.jpg')
    for image in imagen:
        button_image = st.button('Open image')
        if button_image:
            open_image(imagen)
    st.image(imagen, width=300, use_column_width=True)
elif opcion == 'Tipo':
    tipos = df['Tipo'].drop_duplicates()
    tipo = st.sidebar.selectbox('Elige un tipo', tipos)
    imagen = []
    for i in df.index:
        if df['Tipo'][i] == tipo:
            imagen.append('Imagenes/' + df['Imagen'][i] + '.jpg')
    for image in imagen:
        button_image = st.button('Open image')
        if button_image:
            open_image(imagen)
    st.image(imagen, width=300, use_column_width=True)
print('OK')



