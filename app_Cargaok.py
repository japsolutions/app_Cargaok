import streamlit as st
import pandas as pd
import plotly.express as px
import time

def cargar_datos(archivo_datos):
    # Corrección en el parámetro `encoding` y cierre de comillas
    df = pd.read_csv(archivo_datos, encoding="UTF-8", sep=",")
    return df

def main():
    # Título de la aplicación
    st.title("Application to import files & Dowloads BY * Johnny Ahumada Pereira")
    st.write("Sube el archivo CSV de datos para editar, cargar y guardar datos.")


    # Carga de archivo
    archivo_datos = st.file_uploader("Seleccionar archivo CSV para subirlo", type=['csv'])

    if archivo_datos is not None:
        # Cargar datos del archivo
        df = cargar_datos(archivo_datos)

        # Formulario para edición de datos
        with st.form("Formulario de edición de datos"):
            df_editado = st.data_editor(df)
            boton_guardar = st.form_submit_button("Guardar Datos")

        # Generar nombre único para el archivo
        if boton_guardar:
            marca_tiempo = time.strftime("%Y%m%d-%H%M%S")
            nuevo_nombre = f"{archivo_datos.name.split('.')[0]}_{marca_tiempo}.csv"

            # Convertir DataFrame a CSV
            df_final = df_editado.to_csv(index=False, encoding="UTF-8")

            # Botón para descargar el archivo editado (fuera del formulario)
            st.download_button(
                label="Guardar Datos como CSV",
                data=df_final.encode("UTF-8"),
                file_name=nuevo_nombre,
                mime="text/csv",
            )
            st.header(".Get started)
            st.write("11)
            st.bar_chart(df[['educacion', 'implicacion','puesto']]
                          x='educacion',
                          y='puesto')
                     

if __name__ == '__main__':
    # Configuración de la página
    st.set_page_config(page_title="Cargar datos", layout="wide")
    main()
