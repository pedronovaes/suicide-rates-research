import pandas as pd
from src.get_data import get_suicide_data

if __name__ == '__main__':
    # Empty dataframe
    df = pd.DataFrame()

    # Suicide data
    for year in [2000, 2005, 2010, 2015, 2016]:
        temp = get_suicide_data(year=year)
        df = df.append(temp, ignore_index=True)
