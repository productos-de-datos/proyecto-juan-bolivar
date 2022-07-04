"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """


    import urllib.request
    for year in range(1995,2022):
        try:
            urllib.request.urlretrieve("https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/" + str(year) + ".xlsx?raw=true", "data_lake/landing/" + str(year) +".xlsx")
        except:
            urllib.request.urlretrieve("https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/" + str(year) + ".xls?raw=true", "data_lake/landing/" + str(year) +".xls")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ingest_data()
