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
                                'Rank', 'Arrivals M€', 'Squad market value M€', 'Average squad market value M€']]
    df = team_df.copy()
    #df = df.dropna()

    df['Average attendance'] = df['Average attendance'].str.replace(',', '').astype(int)
    df['Year'] = df['Season'].apply(season_to_year)

    #df['Squad market value'] = df['Squad market value'].apply(market_values_to_float)
    df['Squad market value M€'] = df.apply(lambda row: market_values_to_float(row['Squad market value M€'], None), axis=1)
    df['Infl adjusted squad market value M€'] = df.apply(lambda row: market_values_to_float(row['Squad market value M€'], row['Year']), axis=1)

    #df['Average squad market value'] = df['Average squad market value'].apply(market_values_to_float)

    df['Average squad market value M€'] = df.apply(lambda row: market_values_to_float(row['Average squad market value M€'], None), axis=1)
    df['Infl adjusted avg squad market value M€'] = df.apply(lambda row: market_values_to_float(row['Average squad market value M€'], row['Year']), axis=1)

    #df['Arrivals'] = df['Arrivals'].apply(market_values_to_float)
    df['Arrivals M€'] = df.apply(lambda row: market_values_to_float(row['Arrivals M€'], None), axis=1)
    df['Infl adjusted arrivals M€'] = df.apply(lambda row: market_values_to_float(row['Arrivals M€'], row['Year']), axis=1)

    return df

def season_to_year(season):
    suffix = season[:2]
    if suffix == '99' or suffix[0] == '8' or suffix[0] == '7':
        year = int('19' + suffix)
    else:
        year = int('20' + suffix)

    return year

def market_values_to_float(value, year):
    try:
        value = value.replace('€', '').replace('m', '')

        if 'k' in value:
            value = value.replace('k', '')
            #adjust_market_values_to_inflation(value)
            return round(float(float(value) / 1000), 2)
    except AttributeError:
        pass

    if year and value:
        value = adjust_market_values_to_inflation(float(value), year)
    try:
        return round(float(value), 2)
    except TypeError:
        return value

def adjust_market_values_to_inflation(market_value, year):
    CPI_values = {'1999': 72.6, '2000': 73.4, '2001': 74.6, '2002': 75.7, '2003': 76.7, '2004': 77.8, '2005': 79.4,
                         '2006': 81.4, '2007': 83.3, '2008': 86.2, '2009': 87.9, '2010': 90.1, '2011': 93.6,
                         '2012': 96.0, '2013': 98.2, '2014': 99.6, '2015': 100.0, '2016': 100.0, '2017': 103.6,
                         '2018': 106, '2019': 107.8, '2020': 108.9, '2021': 111.6, '2022': 120.5} #source: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l522/mm23, as of 19.2.23
    for key, value in CPI_values.items():
        if key == str(year):
            adjusted_value = round(market_value * (CPI_values['2022']/value), 2)
            return float(adjusted_value)


