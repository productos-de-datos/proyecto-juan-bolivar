def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """

    import numpy as np
    import pandas as pd
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'])
    df_monthly = df.groupby(pd.Grouper(key='fecha', freq='M')).mean().reset_index()
    df_monthly = df_monthly[['fecha','precio']]
    df_monthly.to_csv('data_lake/business/precios-mensuales.csv')

    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    compute_monthly_prices()
    doctest.testmod()
