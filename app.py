import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Análisis de Datos de Vehículos')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
# Convertir la columna 'date_posted' a tipo fecha
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])

if st.sidebar.checkbox('Mostrar explorador de datos'):
    st.subheader('Explorador de Datos Interactivo')
    st.write('Utiliza la tabla para explorar y filtrar los datos.')
    st.dataframe(car_data)  # Asume que car_data es tu DataFrame

st.subheader('Indicadores Clave de Rendimiento')
avg_price = car_data['price'].mean()
avg_odometer = car_data['odometer'].mean()
total_listings = car_data.shape[0]
st.metric(label="Precio Medio", value=f"${avg_price:,.2f}")
st.metric(label="Kilometraje Medio", value=f"{avg_odometer:,.0f} km")
st.metric(label="Total de Anuncios", value=f"{total_listings}")

if st.sidebar.checkbox('Seleccionar columnas específicas'):
    st.subheader('Mostrar Subconjunto de Datos')
    columns_to_show = st.multiselect('Selecciona las columnas que deseas mostrar:', car_data.columns)
    st.dataframe(car_data[columns_to_show])

st.subheader('Resumen de Tendencias')
latest_date = car_data['date_posted'].max()
latest_data = car_data[car_data['date_posted'] == latest_date]
latest_avg_price = latest_data['price'].mean()
delta_price = latest_avg_price - avg_price
st.metric(label="Precio Medio en el Último Día de Publicación", value=f"${latest_avg_price:,.2f}", delta=f"${delta_price:,.2f}")


hist_button = st.button('Histogramade anuncios de venta de coches') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if st.button('Gráfico de Líneas - Precios Medios a lo Largo del Tiempo'):
    st.write('Precios Medios de Vehículos a lo Largo del Tiempo')
    # datos por mes y calcular el precio medio
    data = car_data.groupby(car_data['date_posted'].dt.to_period("M")).price.mean().reset_index(name='average_price')
    # 'date_posted' a string para la serialización de Json
    data['date_posted'] = data['date_posted'].dt.strftime('%Y-%m')
    
    fig = px.line(data, x='date_posted', y='average_price', title='Precios Medios Mensuales de Vehículos')
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
    # Contar la cantidad de vehículos por año de modelo
    data = car_data['model_year'].value_counts().reset_index()
    data.columns = ['model_year', 'count']
    # Asegurarse de que el año del modelo sea un tipo de dato categórico para el eje x
    data['model_year'] = data['model_year'].astype(str)
    # Crear el gráfico
    fig = px.bar(data, x='model_year', y='count', title='Vehículos por Año de Modelo')
    st.plotly_chart(fig, use_container_width=True)


if st.button('Gráfico de Área - Anuncios Publicados a lo Largo del Tiempo'):
    st.write('Anuncios Publicados a lo Largo del Tiempo')
    # datos por mes y contar los anuncios
    data = car_data.groupby(car_data['date_posted'].dt.to_period("M")).size().reset_index(name='count')
    # 'date_posted' a string para la serialización
    data['date_posted'] = data['date_posted'].dt.strftime('%Y-%m')
    
    fig = px.area(data, x='date_posted', y='count', title='Anuncios Publicados por Mes')
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

