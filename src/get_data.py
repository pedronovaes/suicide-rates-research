from pandas_datareader import wb

countries = [
    'AFG', 'ALB', 'DZA', 'AND', 'AGO', 'ATG', 'ARG', 'ARM', 'AUS', 'AUT',
    'AZE', 'BHS', 'BHR', 'BGD', 'BLR', 'BEL', 'BLZ', 'BEN', 'BTN', 'BOL',
    'BIH', 'BWA', 'BRA', 'BRN', 'BGR', 'BFA', 'BDI', 'CPV', 'KHM', 'CMR',
    'CAN', 'CAF', 'TCD', 'CHL', 'CHN', 'COL', 'COM', 'COG', 'CRI', 'CIV',
    'HRV', 'CUB', 'CYP', 'CZE', 'PRK', 'COD', 'DNK', 'DJI', 'DMA', 'DOM',
    'ECU', 'EGY', 'SLV', 'GNQ', 'ERI', 'EST', 'SWZ', 'ETH', 'FJI', 'FIN',
    'FRA', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA', 'GRC', 'GRD', 'GTM', 'GIN',
    'GNB', 'GUY', 'HTI', 'HND', 'HUN', 'ISL', 'IND', 'IDN', 'IRN', 'IRQ',
    'IRL', 'ISR', 'ITA', 'JAM', 'JPN', 'JOR', 'KAZ', 'KEN', 'KIR', 'KWT',
    'KGZ', 'LAO', 'LVA', 'LBN', 'LSO', 'LBR', 'LBY', 'LTU', 'LUX', 'MDG',
    'MWI', 'MYS', 'MDV', 'MLI', 'MLT', 'MHL', 'MRT', 'MUS', 'MEX', 'FSM',
    'MCO', 'MNG', 'MNE', 'MAR', 'MOZ', 'MMR', 'NAM', 'NRU', 'NPL', 'NLD',
    'NZL', 'NIC', 'NER', 'NGA', 'MKD', 'NOR', 'OMN', 'PAK', 'PLW', 'PAN',
    'PNG', 'PRY', 'PER', 'PHL', 'POL', 'PRT', 'QAT', 'KOR', 'MDA', 'RUS',
    'RWA', 'KNA', 'LCA', 'VCT', 'WSM', 'SMR', 'STP', 'SAU', 'SEN', 'SRB',
    'SYC', 'SLE', 'SGP', 'SVK', 'SVN', 'SLB', 'SOM', 'ZAF', 'ESP', 'LKA',
    'SDN', 'SUR', 'SWE', 'CHE', 'SYR', 'TJK', 'THA', 'TLS', 'TGO', 'TON',
    'TTO', 'TUN', 'TUR', 'TKM', 'TUV', 'UGA', 'UKR', 'ARE', 'GBR', 'TZA',
    'USA', 'URY', 'UZB', 'VUT', 'VEN', 'VNM', 'YEM', 'ZMB', 'ZWE'
]


def get_suicide_data(year):
    # Download data
    df = wb.download(country=countries, indicator='SH.STA.SUIC.P5', start=year, end=year) \
           .reset_index() \
           .rename(columns=str.upper) \
           .rename(columns={'SH.STA.SUIC.P5': 'SH.STA.SUIC.P5_{}'.format(year)}) \
           .drop('YEAR', axis=1)

    return df
