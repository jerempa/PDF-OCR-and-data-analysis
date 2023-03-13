from file_operations import file_handling
from data_fetchers import df_operations

teams_that_have_numbers_in_millions = ["Bolton Wanderers", "Brighton & Hove Albion", "Charlton Athletic", "Ipswich Town",
                                       "Leeds United", "Leicester City", "Norwich City", "Queens Park Rangers", "Southampton FC",
                                       "Sunderland AFC", "Wigan Athletic", "Wolverhampton Wanderers"]


def transfermarkt_data_cleansing(team):
    league_level_dicts = file_handling.return_scraped_data_dict("scraped_data7.txt")
    #print(league_level_dicts[0])
    # bpl_df = None
    # for league_level in league_level_dicts:
    #     if league_level:
    #         bpl_df = df_operations.create_df_from_dict(league_level)
    #print(len(league_level_dicts))
   # print(df_operations.create_df_from_dict(league_level_dicts[0]))
    #print(df_operations.create_df_from_dict(league_level_dicts[0])['Team'])
    #print(league_level_dicts)
    #print(league_level_dicts)
    #print(team, 'nice')
    team_df = None
    #print(team, len(league_level_dicts))
    for i in range(0, len(league_level_dicts)):
        if team in df_operations.create_df_from_dict(league_level_dicts[i])['Team'].values:
            team_df = df_operations.create_df_from_dict(league_level_dicts[i])

    #print(bpl_df)
    #print(df_operations.create_df_from_dict(league_level_dicts[1]))

    #return team_df



    mask = team_df['Team'] == team
    team_df = team_df.loc[mask, ['Season', 'League level', 'Total spectators', 'Average attendance', 'Average attendance / capacity %',
                                'Rank', 'Arrivals M€', 'Squad market value M€', 'Average squad market value M€']]
    df = team_df.copy()
    #print(team, df)
    #df = df.dropna()

    df['Average attendance'] = df['Average attendance'].str.replace(',', '').astype(int)
    df['Total spectators'] = df['Total spectators'].str.replace(',', '').astype(int)
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

    df['Position'] = df.apply(lambda row: calculate_position(int(row['Rank']), row['League level']), axis=1)

    return df

def financial_statement_data_cleansing(team):
    league_level_dicts = file_handling.return_scraped_data_dict("financial statement data.txt")
    team_df = df_operations.create_df_from_dict(league_level_dicts[0])

    #print(bpl_df)
    #print(df_operations.create_df_from_dict(league_level_dicts[1]))

    #print(league_level_dicts, team, team_df['Team'], len(team_df['Team']), len(team))
    #print(team_df)

    #return team_df


    #print(type(team_df), len(team_df))
    columns_list = ['years', 'turnover', 'stocks', 'investments', 'tangible assets', 'intangible assets', 'result for the financial year',
                                 'cash at bank and in hand', 'wages', 'creditors: amounts falling due within one year', 'creditors: amounts falling due after more than one year']
    mask = team_df['Team'] == team
    team_df = team_df.loc[mask, columns_list]
    df = team_df.copy()
    #print(team, df)
    df = df.dropna()
    #print(team, df)

    #df['turnover'] = df['turnover'].apply(cleanse_values)
    #df['turnover'] = df['turnover'].str.replace(',', '').astype(int)
    if team in teams_that_have_numbers_in_millions:
        for i in columns_list:
            if i != 'years':
                df[i] = df.apply(lambda row: cleanse_values(row[i], i), axis=1)
        #df['stocks'] = df['stocks'].apply(cleanse_values)
        #df['stocks'] = df.apply(lambda row: cleanse_values(row['stocks'], 'stocks'), axis=1)
    else:
        #print(team)
        df['turnover'] = df.apply(lambda row: cleanse_values(row['turnover'], 'turnover'), axis=1)
        df['result for the financial year'] = df['result for the financial year'].str.replace(',', '').str.replace('(', '-').str.replace(')', '').astype(int)
        for i in columns_list:
            if i not in ['years', 'turnover', 'result for the financial year']:
                #print(i, len(i), "testi", type(df[i]))
                df[i] = df[i].str.replace(',', '').str.replace('(', '').str.replace(')', '').astype(int)

    df['assets'] = df['tangible assets'] + df['intangible assets']
    df['debt'] = df['creditors: amounts falling due within one year'] + df['creditors: amounts falling due after more than one year']
    df['inflation adjusted wages'] = df.apply(lambda row: adjust_values_to_inflation(row['wages'], row['years']), axis=1).astype(int)

    return df

def cleanse_values(value, column):
    #print(value, column)
    value = value.replace(',', '')
    if column == 'turnover':
        if len(value) > 6:
            value = int(value) / 1000
            #value = int(value)
    elif column == 'stocks':
        if len(value) <= 4:
            value = int(value) * 1000
    elif column in ['result for the financial year', 'cash at bank and in hand']:
        if column == 'result for the financial year':
            value = value.replace('(', '-').replace(')', '')
        else:
            value = value.replace('(', '').replace(')', '')
        if len(value) <= 5:
            value = int(value) * 1000
    elif column in ['tangible assets', 'intangible assets', 'wages']:
        if len(value) <= 6:
            value = int(value) * 1000
    elif column in ['creditors: amounts falling due within one year', 'creditors: amounts falling due after more than one year']:
        value = value.replace('(', '').replace(')', '')
        if len(value) <= 6:
            value = int(value) * 1000
    #print(value, column)
    return int(value)
    # return int(value)

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
        value = adjust_values_to_inflation(float(value), year)
    try:
        return round(float(value), 2)
    except TypeError:
        return value

def calculate_position(position, league_level):
    prem_team_count = 20
    champ_team_count = 24
    l1_team_count = 24
    l2_team_count = 24
    pos = None

    #print(position, type(position), league_level)
    if league_level == 'First Tier':
        pos = 93 - position # there are 93 teams in aforementioned leagues so being first in first tier gets max value
    elif league_level == 'Second Tier':
        #print("nice", position, pos)
        pos = 93 - prem_team_count - position
        #print(pos)
    elif league_level == 'Third Tier':
        pos = 93 - prem_team_count - champ_team_count - position
    elif league_level == 'Fourth Tier':
        pos = 93 - prem_team_count - champ_team_count - l1_team_count - position

    return pos

def adjust_values_to_inflation(market_value, year):
    CPI_values = {'1999': 72.6, '2000': 73.4, '2001': 74.6, '2002': 75.7, '2003': 76.7, '2004': 77.8, '2005': 79.4,
                         '2006': 81.4, '2007': 83.3, '2008': 86.2, '2009': 87.9, '2010': 90.1, '2011': 93.6,
                         '2012': 96.0, '2013': 98.2, '2014': 99.6, '2015': 100.0, '2016': 101.0, '2017': 103.6,
                         '2018': 106.0, '2019': 107.8, '2020': 108.9, '2021': 111.6, '2022': 120.5} #source: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l522/mm23, as of 19.2.23
    for key, value in CPI_values.items():
        if key == str(year):
            adjusted_value = round(market_value * (CPI_values['2022']/value), 2)
            return float(adjusted_value)

def pound_to_euro_converter(value, year):
    exhange_rates = {'1999': 1.5195, '2000': 1.6415, '2001': 1.6085, '2002': 1.5908, '2003': 1.4463, '2004': 1.4738, '2005': 1.4625,
                         '2006': 1.4670, '2007': 1.4621, '2008': 1.2593, '2009': 1.1230, '2010': 1.1665, '2011': 1.1527,
                         '2012': 1.2338, '2013': 1.1779, '2014': 1.2409, '2015': 1.3782, '2016': 1.2244, '2017': 1.1413,
                         '2018': 1.1304, '2019': 1.1398, '2020': 1.1250, '2021': 1.1634, '2022': 1.1731} #source: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-gbp.en.html
                                                                                                    #used yearly average
    for key, exhange_value in exhange_rates.items():
        if key == str(year):
            adjusted_value = round(value * exhange_value, 2)
            return float(adjusted_value)



