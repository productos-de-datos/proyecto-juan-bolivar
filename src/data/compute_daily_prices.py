def compute_daily_prices():
    """Compute los precios promedios diarios.
    
    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    import numpy as np
    import pandas as pd
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df_daily = df.groupby('fecha').mean()['precio'].reset_index()
    df_daily.to_csv('data_lake/business/precios-diarios.csv')
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    compute_daily_prices()
