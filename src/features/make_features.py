def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    
    import pandas as pd
    import holidays
    
    df                  = pd.read_csv('data_lake/business/precios-diarios.csv',index_col='Unnamed: 0')
    df['day_of_week']   = pd.to_datetime(df.fecha).dt.dayofweek
    df['day_of_year']   = pd.to_datetime(df.fecha).dt.dayofyear
    df['month_of_year'] = pd.to_datetime(df.fecha).dt.month
    df['year']          = pd.to_datetime(df.fecha).dt.year
    df['holiday'] = pd.to_datetime(df['fecha']).isin(holidays.CO(years=[1995,1996,1997,1998,1999,2000,2001,2002
                                                   ,2003,2004,2005,2006,2007,2008,2009,2010,
                                                   2011,2012,2013,2014,2015,2016,2017,2018,
                                                   2019,2020,2021])).map(lambda x : 1 if x else 0)
    df.to_csv('data_lake/business/features/precios_diarios.csv')
    df.to_csv('data_lake/business/features/precios-diarios.csv')


    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    make_features()
