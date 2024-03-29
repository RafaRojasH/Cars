import streamlit as st
import pandas as pd
from PIL import Image

data = pd.read_csv('carsDB.csv', index_col = False)
df = pd.DataFrame(data, columns=['Nombre', 'Version', 'Pelicula', 'Tipo', 'Observaciones', 'Imagen'])



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
                try:
                    imagen.append('Imagenes/' + df['Imagen'][i] + '.jpeg')
                except:
                    imagen.append('Imagenes/' + df['Imagen'][i] + '.jpg')
        st.image(imagen)
    else:
        for i in df.index:
            if df['Nombre'][i] == nombre:
                try:
                    imagen.append('Imagenes/' + df['Imagen'][i] + '.jpeg')
                except:
                    imagen.append('Imagenes/' + df['Imagen'][i] + '.jpg')
      
        #st.image(imagen)
elif opcion == 'Pelicula':
    peliculas = df['Pelicula'].drop_duplicates()
    pelicula = st.sidebar.selectbox('Elige una película', peliculas)
    imagen = []
    for i in df.index:
        if df['Pelicula'][i] == pelicula:
            try:
                imagen.append('Imagenes/' + df['Imagen'][i] + '.jpeg')
            except:
                imagen.append('Imagenes/' + df['Imagen'][i] + '.jpg')
    
    st.image(imagen)
elif opcion == 'Tipo':
    tipos = df['Tipo'].drop_duplicates()
    tipo = st.sidebar.selectbox('Elige un tipo', tipos)
    imagen = []
    for i in df.index:
        if df['Tipo'][i] == tipo:
            try:
                imagen.append('Imagenes/' + df['Imagen'][i] + '.jpeg')
            except:
                imagen.append('Imagenes/' + df['Imagen'][i] + '.jpg')
    
    st.image(imagen)
print('OK')



