import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Análisis de Datos de Vehículos')

car_data = pd.read_csv('/Users/pedrotrevino/Documents/GitHub_reposit/Sprint4/vehicles_us.csv') # leer los datos
# Convertir la columna 'date_posted' a tipo fecha
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])
hist_button = st.button('Construir histograma') # crear un botón

st.title('Análisis de Datos de Vehículos')
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if st.button('Gráfico de Líneas - Precios Medios a lo Largo del Tiempo'):
    st.write('Precios Medios de Vehículos a lo Largo del Tiempo')
    data = car_data.groupby(car_data['date_posted'].dt.to_period("M")).price.mean()
    fig = px.line(data, title='Precios Medios Mensuales')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Diagrama de Barras - Vehículos por Color'):
    st.write('Cantidad de Vehículos por Color')
    fig = px.bar(car_data, x='paint_color', title='Vehículos por Color')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Gráfico Circular - Tipos de Combustible'):
    st.write('Proporción de Tipos de Combustible')
    fig = px.pie(car_data, names='fuel', title='Tipos de Combustible')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Gráfico de Barras - Vehículos por Año de Modelo'):
    st.write('Cantidad de Vehículos por Año de Modelo')
    fig = px.bar(car_data, x='model_year', title='Vehículos por Año de Modelo')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Gráfico de Área - Anuncios Publicados a lo Largo del Tiempo'):
    st.write('Anuncios Publicados a lo Largo del Tiempo')
    data = car_data.groupby(car_data['date_posted'].dt.to_period("M")).size()
    fig = px.area(data, title='Anuncios Publicados por Mes')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Histograma de Precios'):
    st.write('Histograma de Precios de Vehículos')
    fig = px.histogram(car_data, x='price', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

if st.button('Gráfico de Barras - Tipo de Vehículo'):
    st.write('Conteo por Tipo de Vehículo')
    fig = px.bar(car_data, x='type', title='Conteo por Tipo de Vehículo')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Boxplot - Precios por Tipo de Vehículo'):
    st.write('Distribución de Precios por Tipo de Vehículo')
    fig = px.box(car_data, x='type', y='price', notched=True)
    st.plotly_chart(fig, use_container_width=True)

if st.button('Histograma de Kilometraje'):
    st.write('Histograma de Kilometraje de Vehículos')
    fig = px.histogram(car_data, x='odometer', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

if st.button('Gráfico de Dispersión - Precio vs. Kilometraje'):
    st.write('Relación entre Precio y Kilometraje')
    fig = px.scatter(car_data, x='odometer', y='price', trendline='ols')
    st.plotly_chart(fig, use_container_width=True)

