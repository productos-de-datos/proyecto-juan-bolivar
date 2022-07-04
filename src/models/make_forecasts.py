def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.

    """

    import pandas as pd
    import pickle
    import pdb
    
    fechas=['2001-05-06','2010-10-01','2013-04-21','2019-07-15','2020-06-15']
    df  = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    df_output = df[ df['fecha'].isin(fechas) ]
    loaded_model = pickle.load(open('models/precios-diarios.pkl', 'rb'))
    X = df_output[['day_of_week','day_of_year','month_of_year','year','holiday']]
    y = df_output['precio']
    y_predict = loaded_model.predict(X)

    df_out = pd.DataFrame({'fechas':fechas,'precio_promedio_real':y,'precio_pronostico_promedio':y_predict})

    df_out.to_csv('data_lake/business/forecasts/precios-diarios.csv')
    


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()
