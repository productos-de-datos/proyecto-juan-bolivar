def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.

    """
    import pandas as pd
    import os, glob
    import pdb

    files = glob.glob('data_lake/raw/*')
    df_complete = pd.DataFrame(columns=['fecha','hora','precio'])

    for file in files:
        df         = pd.read_csv(file,skiprows=2,header=None,usecols=range(26))
        df.columns = ['Index','Fecha','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
        df_fixed = pd.melt(df, id_vars=['Fecha'], value_vars=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']).rename(columns={'Fecha':'fecha','variable':'hora','value':'precio'})
        df_complete = pd.concat([df_complete,df_fixed])
    df_complete = df_complete[df_complete["fecha"]!="Fecha"]
    df_complete['fecha'] = pd.to_datetime(df_complete['fecha'])
    df_complete = df_complete.dropna(subset='fecha')
    df_complete = df_complete.sort_values(by=['fecha','hora']).reset_index()
    df_complete = df_complete.drop(columns='index')
    df_complete['precio'] = df_complete['precio'].fillna(method='bfill')
    #raise NotImplementedError("Implementar esta función")
    df_complete.to_csv('data_lake/cleansed/precios-horarios.csv')


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    clean_data()
