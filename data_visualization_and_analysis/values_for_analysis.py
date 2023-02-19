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
    bpl_df = df_operations.create_df_from_dict(league_level_dicts[0])
    print(bpl_df)
    mask = bpl_df['Team'] == team
    team_df = bpl_df.loc[mask, ['Season', 'League level', 'Average attendance', 'Average attendance / capacity %',
                                'Rank', 'Arrivals', 'Squad market value', 'Average squad market value']]
    df = team_df.copy()
    df = df.dropna()

    df['Average attendance'] = df['Average attendance'].str.replace(',', '').astype(int)
    df['Year'] = df['Season'].apply(season_to_year)

    df['Squad market value'] = df['Squad market value'].apply(market_values_to_float)
    df['Average squad market value'] = df['Average squad market value'].apply(market_values_to_float)
    df['Arrivals'] = df['Arrivals'].apply(market_values_to_float)

    return df

def season_to_year(season):
    suffix = season[:2]
    if suffix == '99':
        year = int('19' + suffix)
    else:
        year = int('20' + suffix)
    return year

def market_values_to_float(value):
    value = value.replace('€', '').replace('m', '')
    if 'k' in value:
        value = value.replace('k', '')
        return float(float(value) / 1000)
    return float(value)