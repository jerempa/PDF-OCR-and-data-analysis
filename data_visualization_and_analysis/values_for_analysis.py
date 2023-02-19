from file_operations import file_handling
from data_fetchers import df_operations

import pandas as pd


def league_tier_throughout_years(team):
    league_level_dicts = file_handling.return_scraped_data_dict()
    #print(league_level_dicts[0])
    # bpl_df = None
    # for league_level in league_level_dicts:
    #     if league_level:
    #         bpl_df = df_operations.create_df_from_dict(league_level)
    #print(len(league_level_dicts))
   # print(df_operations.create_df_from_dict(league_level_dicts[0]))
    #print(df_operations.create_df_from_dict(league_level_dicts[0])['Team'])
    team_df = None
    for i in range(0, len(league_level_dicts) - 1):
        if team in df_operations.create_df_from_dict(league_level_dicts[i])['Team'].values:
            team_df = df_operations.create_df_from_dict(league_level_dicts[i])

    #print(bpl_df)
    #print(df_operations.create_df_from_dict(league_level_dicts[1]))


    mask = team_df['Team'] == team
    team_df = team_df.loc[mask, ['Season', 'League level', 'Average attendance', 'Average attendance / capacity %',
                                'Rank', 'Arrivals', 'Squad market value', 'Average squad market value']]
    df = team_df.copy()
    df = df.dropna()

    df['Average attendance'] = df['Average attendance'].str.replace(',', '').astype(int)
    df['Year'] = df['Season'].apply(season_to_year)

    df['Squad market value'] = df['Squad market value'].apply(market_values_to_float)
    df['Average squad market value'] = df['Average squad market value'].apply(market_values_to_float)
    #df.apply(lambda row: market_values_to_float(row['Average squad market value'], row['Year']), axis=1)
    df['Arrivals'] = df['Arrivals'].apply(market_values_to_float)

    return df

def season_to_year(season):
    suffix = season[:2]
    if suffix == '99' or suffix[0] == '8' or suffix[0] == '7':
        year = int('19' + suffix)
    else:
        year = int('20' + suffix)

    return year

def market_values_to_float(value):
    #print(value)
    value = value.replace('€', '').replace('m', '')
    if 'k' in value:
        value = value.replace('k', '')
        #adjust_market_values_to_inflation(value)
        return float(float(value) / 1000)

    return float(value)

def adjust_market_values_to_inflation(market_value):
    CPI_values = {'2000': 73.4, '2001': 74.6, '2002': 75.7, '2003': 76.7, '2004': 77.8, '2005': 79.4,
                         '2006': 81.4, '2007': 83.3, '2008': 86.2, '2009': 87.9, '2010': 90.1, '2011': 93.6,
                         '2012': 96.0, '2013': 98.2, '2014': 99.6, '2015': 100.0, '2016': 100.0, '2017': 103.6,
                         '2018': 106, '2019': 107.8, '2020': 108.9, '2021': 111.6, '2022': 120.5} #source: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l522/mm23, as of 19.2.23

    for year, value in CPI_values.items():
        adjusted_value = market_value * value/CPI_values['2022']
        if year == '2004':
            break


