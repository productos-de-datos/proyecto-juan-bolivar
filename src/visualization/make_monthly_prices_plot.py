def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.
    
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pdb
    import pandas as pd
    import matplotlib.ticker as ticker

    df = pd.read_csv('data_lake/business/precios-mensuales.csv')
    plot = sns.lineplot(data=df,x="fecha",y="precio" )
    plt.xticks(rotation=90)
    plot.xaxis.set_major_locator(ticker.LinearLocator(40))
    plt.tight_layout()
    fig = plot.get_figure()
    fig.savefig("data_lake/business/reports/figures/monthly_prices.png") 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    make_monthly_prices_plot()
