from file_operations import file_handling
from data_fetchers import df_operations

import numpy as np

teams_that_have_numbers_in_millions = ["Bolton Wanderers", "Charlton Athletic", "Ipswich Town",
                                       "Leeds United", "Leicester City", "Norwich City", "Queens Park Rangers", "Southampton FC",
                                       "Sunderland AFC", "Wolverhampton Wanderers"]


def transfermarkt_data_cleansing(team, bool):
    league_level_dicts = file_handling.return_scraped_data_dict("scraped_data7.txt")
    #print(league_level_dicts)
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
    #print(league_level_dicts)
    team_df = None
    #print(l)
    # print(league_level_dicts[0])
    # print(league_level_dicts[1])
    # print(league_level_dicts[2])
    #team_df = df_operations.create_df_from_dict(league_level_dicts[0])
    #print(team_df['Rank'], team_df['League level'])
    for i in range(0, len(league_level_dicts)):
        if team in df_operations.create_df_from_dict(league_level_dicts[i])['Team'].values:
            team_df = df_operations.create_df_from_dict(league_level_dicts[i])

    #print(bpl_df)
    #print(df_operations.create_df_from_dict(league_level_dicts[1]))

    #print(team_df)

    #return team_df
    #print(team_df['Team'])



    mask = team_df['Team'] == team
    team_df = team_df.loc[mask, ['Season', 'League level', 'Total spectators', 'Average attendance', 'Average attendance / capacity %', 'Stadium capacity', 'City population',
                                'Rank', 'Arrivals M€', 'Departures M€', 'Squad market value M€', 'Average squad market value M€', 'Average squad age',
                                'Distance to the nearest major city (km)', 'Only football team in top 4 leagues in the metropolitan county', 'Manager', 'City has a professional rugby team']]
    df = team_df.copy()
    #print(team, df)
    #df = df.dropna()

    df['Average attendance'] = df['Average attendance'].str.replace(',', '').astype(int)
    df['Ln(Average attendance)'] = np.sqrt(df['Average attendance'])
    df['Total spectators'] = df['Total spectators'].str.replace(',', '').astype(int)
    df['Stadium capacity'] = df['Stadium capacity'].str.replace(',', '').astype(int)
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
    df['Ln(Infl adjusted arrivals M€)'] = np.log1p(df['Infl adjusted arrivals M€'])

    df['Departures M€'] = df.apply(lambda row: market_values_to_float(row['Departures M€'], None), axis=1)
    df['Infl adjusted departures M€'] = df.apply(lambda row: market_values_to_float(row['Departures M€'], row['Year']), axis=1)


    df['Ln(Infl adjusted squad market value M€)'] = np.log(df['Infl adjusted squad market value M€'])
    df['Ln(Infl adjusted avg squad market value M€)'] = np.log(df['Infl adjusted avg squad market value M€'])

    df['Overall position'] = df.apply(lambda row: calculate_position(int(row['Rank']), row['League level']), axis=1)

    #df['(Distance to the nearest major city (km))^2'] = df['Distance to the nearest major city (km)']**2


    df['(Squad size)^2'] = df.apply(lambda row: calculate_squad_size(row['Squad market value M€'], row['Average squad market value M€']), axis=1)**2

    df['Managerial change'] = df.apply(lambda row: determine_if_manager_was_changed(row['Manager'], df['Manager'].shift(-1).loc[row.name]), axis=1)

    df['(Average squad age (years))^2'] = round(df['Average squad age'].astype(float)**2, 2)

    df['Ln(City population)'] = np.log(df['City population'])

    df['Stadium capacity (thousands)'] = df['Stadium capacity'] / 1000

    df['The league in which team is in'] = df.apply(lambda row: which_league_team_in(row['Overall position'], "Prem"), axis=1).astype(int)

    # df['Team is in the Championship'] = df.apply(lambda row: which_league_team_in(row['Position'], "Champ"), axis=1).astype(int)
    #
    # df['Team is in League One'] = df.apply(lambda row: which_league_team_in(row['Position'], "L1"), axis=1).astype(int)
    #
    # df['Team is in League Two'] = df.apply(lambda row: which_league_team_in(row['Position'], "L2"), axis=1).astype(int)

    df['Transfer spending'] = df.apply(lambda row: calculate_transfer_spending(row['Infl adjusted arrivals M€'], row['Infl adjusted departures M€']), axis=1)

    df['Team'] = team

    df['Average attendance / capacity %^2'] = (df['Average attendance / capacity %']**2).astype(float)

    if bool:

        df = df.iloc[1:len(df['Team']) - 5]

        df = df.drop(df.index[1]) #drop covid row




    #df['Avg attendance (thousands)'] = df['Average attendance'] / 1000

    #print(df['Managerial change'], df['Year'], df['Season'])

    return df

def financial_statement_data_cleansing(team):
    league_level_dicts = file_handling.return_scraped_data_dict("financial statement data.txt")
    team_df = df_operations.create_df_from_dict(league_level_dicts[0])

    df_for_pos = transfermarkt_data_cleansing(team, False)
    df_for_pos = df_for_pos.iloc[1:-2]
    #df_for_pos = df_for_pos.iloc[1:-1]
    columns_list = ['years', 'turnover', 'result for the financial year', 'wages']
    mask = team_df['Team'] == team
    team_df = team_df.loc[mask, columns_list]
    df = team_df.copy()
    df = df.iloc[2:]

    position = df_for_pos['Overall position'].tolist()
    position.pop(0)
    position.insert(-1, 0) #shifting the values by one index

    capacity = df_for_pos['Stadium capacity (thousands)'].tolist()
    population = df_for_pos['Ln(City population)'].tolist()
    only_team = df_for_pos['Only football team in top 4 leagues in the metropolitan county'].tolist()

    has_rugby = df_for_pos['City has a professional rugby team'].tolist()
    squad_size = df_for_pos['(Squad size)^2'].tolist()
    avg_squad_age = df_for_pos['(Average squad age (years))^2'].tolist()
    avg_squad_age = df_for_pos['(Average squad age (years))^2'].tolist()
    league_level = df_for_pos['League level'].tolist()


    transfer_spending = df_for_pos['Transfer spending'].tolist()
    transfer_spending.pop(0)
    transfer_spending.insert(-1, 0) #shifting the values by one index

    team_in_prem = df_for_pos['The league in which team is in'].tolist()
    team_in_prem.pop(0)
    team_in_prem.insert(-1, 0) #shifting the values by one index

    # team_in_champ = df_for_pos['Team is in the Championship'].tolist()
    # team_in_champ.pop(0)
    # team_in_champ.insert(-1, 0) #shifting the values by one index
    #
    # team_in_l1 = df_for_pos['Team is in League One'].tolist()
    # team_in_l1.pop(0)
    # team_in_l1.insert(-1, 0) #shifting the values by one index
    #
    # team_in_l2 = df_for_pos['Team is in League Two'].tolist()
    # team_in_l2.pop(0)
    # team_in_l2.insert(-1, 0) #shifting the values by one index

    # #print(df_for_pos['Position'].tolist())

    position.reverse()
    capacity.reverse()
    population.reverse()
    squad_size.reverse()
    avg_squad_age.reverse()
    team_in_prem.reverse()
    league_level.reverse()
    # team_in_champ.reverse()
    # team_in_l1.reverse()
    # team_in_l2.reverse()
    transfer_spending.reverse()

    # print(len(position), position)
    # print(len(population), population)
    # print(len(capacity), capacity)
    # print(position)
    # position.insert(0, 0)
    # capacity.insert(0, 0)
    # population.insert(0, 0)
    # only_team.insert(0, 0)
    # has_rugby.insert(0, 0)

    df['Overall position'] = position
    #print(df['Position'])
    df['Stadium capacity (thousands)'] = capacity
    df['Ln(City population)'] = population
    df['Only football team in top 4 leagues in the metropolitan county'] = only_team
    df['City has a professional rugby team'] = has_rugby
    df['Transfer spending'] = transfer_spending
    df['(Squad size)^2'] = squad_size
    df['(Average squad age (years))^2'] = avg_squad_age
    df['The league in which team is in'] = team_in_prem
    df['League level'] = league_level
    # df['Team is in the Championship'] = team_in_champ
    # df['Team is in League One'] = team_in_l1
    # df['Team is in League Two'] = team_in_l2

    df = df.drop(df.index[-2]) #drop covid row

    #print(df)
    # print(position, len(position))
    #df['position'] = df_for_pos['Position']
    #print(df)
    #print(df[])
    df['team'] = team
    df = df.dropna()

    #df['turnover'] = df['turnover'].apply(cleanse_values)
    #df['turnover'] = df['turnover'].str.replace(',', '').astype(int)
    if team in teams_that_have_numbers_in_millions:
        for i in columns_list:
            if i != 'years':
                df[i] = df.apply(lambda row: cleanse_values(row[i], i, row['years']), axis=1)
                if i == 'result for the financial year':
                    df[f'1 / {i}'] = df[i]
                else:
                    df[f'Ln({i})'] = np.log(df[i])
        #df['stocks'] = df['stocks'].apply(cleanse_values)
        #df['stocks'] = df.apply(lambda row: cleanse_values(row['stocks'], 'stocks'), axis=1)
    else:
        #print(team)
        df['turnover'] = df.apply(lambda row: cleanse_values(row['turnover'], 'turnover', row['years']), axis=1)
        df['Ln(turnover)'] = np.log(df['turnover'])
        df['result for the financial year'] = df['result for the financial year'].str.replace(',', '').str.replace('(', '-').str.replace(')', '').astype(int)
        df['1 / result for the financial year'] = df.apply(lambda row: pound_to_euro_converter(row['result for the financial year'], row['years']), axis=1)
        for i in columns_list:
            if i not in ['years', 'turnover', 'result for the financial year']:
                #print(i, len(i), "testi", type(df[i]))
                df[i] = df[i].str.replace(',', '').str.replace('(', '').str.replace(')', '').astype(int)
                df[i] = df.apply(lambda row: pound_to_euro_converter(row[i], row['years']), axis=1)
                #df[f'L']

    #df['Ln(assets)'] = np.log((df['tangible assets'] + df['intangible assets'] + df['stocks'] + df['investments'] + df['cash at bank and in hand'] + df['debtors']))
    #df['Ln(debt)'] = np.log((df['creditors: amounts falling due within one year'] + df['creditors: amounts falling due after more than one year']))
    df['Ln(inflation adjusted wages)'] = np.log(df.apply(lambda row: adjust_values_to_inflation(row['wages'], row['years']), axis=1).astype(int))
    df['year'] = df['years'].astype(int)
    #df['Team is in the Premier League'] = df.apply(lambda row: team_is_in_premier_league(row['Position']), axis=1).astype(int)

    # if team in teams_that_have_numbers_in_millions:
    #     for i in columns_list:
    #         if i != 'years':
    #             df[i] = df.apply(lambda row: cleanse_values(row[i], i, row['years']), axis=1)
    #     #df['stocks'] = df['stocks'].apply(cleanse_values)
    #     #df['stocks'] = df.apply(lambda row: cleanse_values(row['stocks'], 'stocks'), axis=1)
    # else:
    #     #print(team)
    #     df['turnover'] = df.apply(lambda row: cleanse_values(row['turnover'], 'turnover', row['years']), axis=1)
    #     df['result for the financial year'] = df['result for the financial year'].str.replace(',', '').str.replace('(', '-').str.replace(')', '').astype(int)
    #     df['result for the financial year'] = df.apply(lambda row: pound_to_euro_converter(row['result for the financial year'], row['years']), axis=1)
    #     for i in columns_list:
    #         if i not in ['years', 'turnover', 'result for the financial year']:
    #             #print(i, len(i), "testi", type(df[i]))
    #             df[i] = df[i].str.replace(',', '').str.replace('(', '').str.replace(')', '').astype(int)
    #             df[i] = df.apply(lambda row: pound_to_euro_converter(row[i], row['years']), axis=1)
    #
    # df['assets'] = (df['tangible assets'] + df['intangible assets'] + df['stocks'] + df['investments'] + df['cash at bank and in hand'] + df['debtors']) / 1000
    # df['debt'] = (df['creditors: amounts falling due within one year'] + df['creditors: amounts falling due after more than one year']) / 1000
    # df['inflation adjusted wages'] = df.apply(lambda row: adjust_values_to_inflation(row['wages'], row['years']) / 1000, axis=1).astype(int)
    # print(df_for_pos['Position'], len(df_for_pos['Position']))
    # print(len(df['assets']), len(df['debt']), len(df['inflation adjusted wages']), len(df['turnover']), len(df['result for the financial year']), len(df['years']))
    # for i in columns_list:
    #     print(len(df[i]), i, len(df[i].tolist()))
    # print(len(df['assets']), 'test')
    # #df_for_pos['Position'] = df_for_pos.drop([24, 25])
    # print(df_for_pos['Position'], len(df_for_pos['Position']))
    # position = df_for_pos['Position'].tolist()
    #print(df_for_pos['Position'].tolist())
    # position.reverse()
    # # print(position, len(position))
    # position.insert(0, 0)
    # print(position, len(position))
    # print(df_for_pos['Position'])
    #print(df)

    return df

def cleanse_values(value, column, year):
    #print(value, column)
    value = value.replace(',', '')
    if column == 'turnover':
        #print(type(year), year)
        if year == "1999" and len(value) == 6:
            pass
        else:
            if len(value) <= 6:
                value = int(value) * 1000
                #value = int(value)
    elif column == 'stocks':
        if len(value) <= 4:
            value = int(value) * 1000
    elif column in ['result for the financial year', 'cash at bank and in hand']:
        if column == 'result for the financial year':
            value = value.replace('(', '-').replace(')', '')
        else:
            value = value.replace('(', '').replace(')', '')
        if len(value) <= 5 or (value[0] == '-' and len(value) == 6):
            value = int(value) * 1000
    elif column in ['tangible assets', 'intangible assets', 'wages', 'debtors']:
        if len(value) <= 5:
            value = int(value) * 1000
    elif column in ['creditors: amounts falling due within one year', 'creditors: amounts falling due after more than one year']:
        value = value.replace('(', '').replace(')', '')
        if len(value) <= 6:
            value = int(value) * 1000
    value = pound_to_euro_converter(int(value), year)

    # if column == 'turnover':
    #     value = int(value) / 1000000
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
    #print(position, league_level)

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

def calculate_squad_size(market_value, avg_market_value):
    #print(market_value, avg_market_value)
    try:
        squad_size = int(round(market_value / avg_market_value))

        #print(squad_size, market_value)

        return squad_size
    except ValueError:
        pass

def determine_if_manager_was_changed(manager, last_season_manager):
    if manager != last_season_manager:
        return 1
    return 0

def which_league_team_in(position, league):
    if position >= 73:
        return 4
    elif position >= 49:
        return 3
    elif position >= 25:
        return 2
    else:
        return 1

def calculate_transfer_spending(bought, sold):
    #print(bought, sold)
    return float(sold - bought)


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
    for key, exhange_value in exhange_rates.items():
        if key == str(year):
            adjusted_value = round(value * exhange_value, 2)
            return float(adjusted_value)



