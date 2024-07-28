import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.replace(to_replace={'quantity':[None]}, value=0)