"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""


import sys
from ingest_data import *
from transform_data import *
from clean_data import *
from compute_daily_prices import * 
from compute_monthly_prices import *
sys.path.append('src/visualization')
sys.path.append('src/features')
sys.path.append('src/models')

from make_daily_prices_plot import *
from make_monthly_prices_plot import *
from make_features import *
from train_daily_model import *
from make_forecasts import *


import luigi

class get_data(luigi.Task):
    """
    Aggregate the count results from the different files
    """

  
    def output(self):
        return luigi.LocalTarget("data_lake/cleansed/precios-horarios.csv")

    def run(self):
        ingest_data()
        transform_data()
        clean_data()

class calculate_data(luigi.Task):
    """
    Task to compilate information about monthly means and daily means
    """

    def requires(self):
        return get_data()

    def output(self):
        return luigi.LocalTarget("data_lake/business/precios-diarios.csv")

    def run(self):
        compute_daily_prices()
        compute_monthly_prices()
        make_daily_prices_plot()
        make_monthly_prices_plot()
        make_features()
        train_daily_model()
        make_forecasts()
        
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    luigi.build([calculate_data()],local_scheduler=True)
    
