from data_visualization_and_analysis import values_for_analysis
from error_handling import errors
from file_operations import file_handling

import statistics

teams = ['Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
         'Blackburn Rovers', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Queens Park Rangers', 'Wigan Athletic',
         'Bolton Wanderers', 'Charlton Athletic', 'Derby County', 'Ipswich Town', 'Portsmouth FC']

def main():
    #values_dict = {}
    for team in teams:
        df = values_for_analysis.league_tier_throughout_years(team)
        #print(df)
        show_average_attendace_to_capacity(df, team)
        #bought_players_avg_and_median(df, team)
        #squad_value_avg_median(df, team)
        #avg_squad_value_avg_median(df, team)

def show_average_attendace_to_capacity(df, team):
    premier_league_attendance = []
    championship_attendance = []
    league_one_attendance = []

    for index, row in df.iterrows():
        if row['Average attendance / capacity %'] > 2.00 and row['Year'] > 1990: #don't take into account covid year without spectators
            if row['League level'] == 'First Tier':
                premier_league_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Second Tier':
                championship_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Third Tier':
                league_one_attendance.append(row['Average attendance / capacity %'])
    data = []

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_attendance)
    championship_median, championship_avg = errors.median_avg_errors(championship_attendance)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_attendance)

    data.append(team)
    data.append(premier_league_median)
    data.append(premier_league_avg)

    data.append(championship_median)
    data.append(championship_avg)

    data.append(league_one_median)
    data.append(league_one_avg)

    file_handling.calculations_to_csv(data)

def bought_players_avg_and_median(df, team):
    premier_league_arrivals = []
    championship_arrivals = []
    league_one_arrivals = []
    print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 1990:
            if row['League level'] == 'First Tier':
                premier_league_arrivals.append(row['Infl adjusted arrivals M€'])
            elif row['League level'] == 'Second Tier':
                championship_arrivals.append(row['Infl adjusted arrivals M€'])
            elif row['League level'] == 'Third Tier':
                league_one_arrivals.append(row['Infl adjusted arrivals M€'])
    #print(premier_league_arrivals, championship_arrivals, league_one_arrivals)
    try:
        print(f'Median Premier League: {round(statistics.median(premier_league_arrivals), 2)} M€'
              f' Median Championship: {round(statistics.median(championship_arrivals), 2)} M€')
              #f' Median League One: {round(statistics.median(league_one_arrivals), 2)} M€')
    except statistics.StatisticsError:
        pass
    try:
        print(f'Average Premier League: {round(sum(premier_league_arrivals) / len(premier_league_arrivals), 2)} M€'
              f' Average Championship: {round(sum(championship_arrivals) / len(championship_arrivals), 2)} M€')
              #f' Average League One: {round(sum(league_one_arrivals) / len(league_one_arrivals), 2)} M€')
    except ZeroDivisionError:
        pass

def squad_value_avd_median(df, team):
    premier_league_squad_value = []
    championship_squad_value = []
    league_one_squad_value = []
    print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 1990:
            if row['League level'] == 'First Tier':
                premier_league_squad_value.append(row['Infl adjusted squad market value M€'])
            elif row['League level'] == 'Second Tier':
                championship_squad_value.append(row['Infl adjusted squad market value M€'])
            elif row['League level'] == 'Third Tier':
                league_one_squad_value.append(row['Infl adjusted squad market value M€'])
    #print(premier_league_arrivals, championship_arrivals, league_one_arrivals)
    try:
        print(f'Median Premier League: {round(statistics.median(premier_league_squad_value), 2)} M€'
              f' Median Championship: {round(statistics.median(championship_squad_value), 2)} M€')
              #f' Median League One: {round(statistics.median(league_one_arrivals), 2)} M€')
    except statistics.StatisticsError:
        pass
    try:
        print(f'Average Premier League: {round(sum(premier_league_squad_value) / len(premier_league_squad_value), 2)} M€'
              f' Average Championship: {round(sum(championship_squad_value) / len(championship_squad_value), 2)} M€')
              #f' Average League One: {round(sum(league_one_arrivals) / len(league_one_arrivals), 2)} M€')
    except ZeroDivisionError:
        pass

def avg_squad_value_avd_median(df, team):
    premier_league_avg_squad_value = []
    championship_avg_squad_value = []
    league_one_avg_squad_value = []
    print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 1990:
            if row['League level'] == 'First Tier':
                premier_league_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
            elif row['League level'] == 'Second Tier':
                championship_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
            elif row['League level'] == 'Third Tier':
                league_one_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
    #print(premier_league_arrivals, championship_arrivals, league_one_arrivals)
    try:
        print(f'Median Premier League: {round(statistics.median(premier_league_avg_squad_value), 2)} M€'
              f' Median Championship: {round(statistics.median(championship_avg_squad_value), 2)} M€')
              #f' Median League One: {round(statistics.median(league_one_arrivals), 2)} M€')
    except statistics.StatisticsError:
        pass
    try:
        print(f'Average Premier League: {round(sum(premier_league_avg_squad_value) / len(premier_league_avg_squad_value), 2)} M€'
              f' Average Championship: {round(sum(championship_avg_squad_value) / len(championship_avg_squad_value), 2)} M€')
              #f' Average League One: {round(sum(league_one_arrivals) / len(league_one_arrivals), 2)} M€')
    except ZeroDivisionError:
        pass

