def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """

    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    import pandas as pd
    import pickle

    df = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    X = df[['day_of_week','day_of_year','month_of_year','year','holiday']]
    y = df['precio']
    X_train, X_test, y_train, y_test = train_test_split(X, y , train_size=0.9)
    regr = RandomForestRegressor()
    regr.fit(X_train, y_train)
    pickle.dump(regr, open('models/precios-diarios.pkl', 'wb'))
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()
