def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
    """

    from pathlib import Path
    Path("data_lake/landing").mkdir(parents=True, exist_ok=True)
    Path("data_lake/raw").mkdir(parents=True, exist_ok=True)
    Path("data_lake/cleansed").mkdir(parents=True, exist_ok=True)
    Path("data_lake/business").mkdir(parents=True, exist_ok=True)
    Path("data_lake/business/reports/figures").mkdir(parents=True, exist_ok=True)
    Path("data_lake/business/features").mkdir(parents=True, exist_ok=True)
    Path("data_lake/business/forecasts").mkdir(parents=True, exist_ok=True)
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    create_data_lake()
    doctest.testmod()
