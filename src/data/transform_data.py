def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    #raise NotImplementedError("Implementar esta función")

    import os,glob
    import pandas as pd

    landing_dir = "data_lake/landing/"
    files = glob.glob(landing_dir + "*")

    for file in files:
        path_excel_file =os.path.basename(file)
        name_file = path_excel_file.split('.')[0]
        pd.read_excel(file).to_csv('data_lake/raw/' + name_file + '.csv')

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
