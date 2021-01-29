import pandas as pd
from src.get_data import get_wb_data


if __name__ == '__main__':
    # Empty dataframe
    df = pd.DataFrame()

    # Suicide data
    for year in [2000, 2005, 2010, 2015, 2016]:
        suicide = get_wb_data(indicator='SH.STA.SUIC.P5', year=year)
        unemployment = get_wb_data(indicator='SL.UEM.TOTL.ZS', year=year)

        temp = pd.merge(left=suicide, right=unemployment, how='outer', on=['COUNTRY', 'YEAR'])

        df = df.append(temp, ignore_index=True)
