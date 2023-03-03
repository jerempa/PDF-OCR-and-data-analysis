from data_visualization_and_analysis import values_for_analysis
from error_handling import errors
from file_operations import file_handling
from data_fetchers import df_operations

import numpy as np
import statistics


teams = ['Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
         'Blackburn Rovers', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Queens Park Rangers', 'Wigan Athletic',
         'Bolton Wanderers', 'Charlton Athletic', 'Derby County', 'Ipswich Town', 'Portsmouth FC']

# teams = ['Blackburn Rovers', 'Blackpool FC', 'Bolton Wanderers', 'Brentford FC', 'Brighton & Hove Albion',
#          'Charlton Athletic', 'Derby County', 'Huddersfield Town', 'Hull City', 'Ipswich Town', 'Leeds United',
#          'Leicester City', 'Norwich City', 'Nottingham Forest', 'Portsmouth FC', 'Queens Park Rangers',
#          'Southampton FC', 'Wigan Athletic', 'Wolverhampton Wanderers']

def main():
    dfs = []
    for team in teams:
        df = values_for_analysis.league_tier_throughout_years(team)
        print(team, df)
        dfs.append(df)

    concat_df = df_operations.concat_dfs(dfs)
    #print(concat_df)


    #print(concat_df)
    #print(concat_df)
        #print(type(df))
        #print(team, df)
    #show_average_attendace_to_capacity(concat_df, "Total")
    #bought_players_avg_and_median(concat_df, "Total")
    #squad_value_avg_median(concat_df, "Total")
    #avg_squad_value_avg_median(concat_df, "Total")

def show_average_attendace_to_capacity(df, team):
    premier_league_attendance = []
    championship_attendance = []
    league_one_attendance = []
    league_two_attendance = []

    for index, row in df.iterrows():
        if row['Average attendance / capacity %'] > 2.00 and row['Year'] > 1990: #don't take into account covid year without spectators
            if row['League level'] == 'First Tier':
                premier_league_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Second Tier':
                championship_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Third Tier':
                league_one_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Fourth Tier':
                league_two_attendance.append(row['Average attendance / capacity %'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_attendance)
    championship_median, championship_avg = errors.median_avg_errors(championship_attendance)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_attendance)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_attendance)


    data = append_values_to_data(team, premier_league_median, premier_league_avg, championship_median, championship_avg, league_one_median, league_one_avg, league_two_median, league_two_avg)


    file_handling.calculations_to_csv("all_values.csv", "Average attendance / capacity %", data)

def bought_players_avg_and_median(df, team):
    premier_league_arrivals = []
    championship_arrivals = []
    league_one_arrivals = []
    league_two_arrivals = []
    #print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 1990:
            if row['League level'] == 'First Tier':
                premier_league_arrivals.append(row['Infl adjusted arrivals M€'])
            elif row['League level'] == 'Second Tier':
                championship_arrivals.append(row['Infl adjusted arrivals M€'])
            elif row['League level'] == 'Third Tier':
                league_one_arrivals.append(row['Infl adjusted arrivals M€'])
            elif row['League level'] == 'Fourth Tier':
                league_two_arrivals.append(row['Infl adjusted arrivals M€'])
    #print(df)
    #print(team, premier_league_arrivals, championship_arrivals, league_one_arrivals, league_two_arrivals)


    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_arrivals)
    championship_median, championship_avg = errors.median_avg_errors(championship_arrivals)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_arrivals)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_arrivals)

    data = append_values_to_data(team, premier_league_median, premier_league_avg, championship_median, championship_avg,
                                 league_one_median, league_one_avg, league_two_median, league_two_avg)

    file_handling.calculations_to_csv("all_values.csv", "Inflation adjusted arrivals M€", data)

def squad_value_avg_median(df, team):
    premier_league_squad_value = []
    championship_squad_value = []
    league_one_squad_value = []
    league_two_squad_value = []
    #print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 2003: #don't take into account years that don't have values
            if row['League level'] == 'First Tier':
                premier_league_squad_value.append(row['Infl adjusted squad market value M€'])
            elif row['League level'] == 'Second Tier':
                championship_squad_value.append(row['Infl adjusted squad market value M€'])
            elif row['League level'] == 'Third Tier':
                league_one_squad_value.append(row['Infl adjusted squad market value M€'])
            elif row['League level'] == 'Fourth Tier':
                league_two_squad_value.append(row['Infl adjusted squad market value M€'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_squad_value)
    championship_median, championship_avg = errors.median_avg_errors(championship_squad_value)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_squad_value)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_squad_value)

    data = append_values_to_data(team, premier_league_median, premier_league_avg, championship_median, championship_avg,
                                 league_one_median, league_one_avg, league_two_median, league_two_avg)

    file_handling.calculations_to_csv("all_values.csv", "Inflation adjusted squad value M€", data)

def avg_squad_value_avg_median(df, team):
    premier_league_avg_squad_value = []
    championship_avg_squad_value = []
    league_one_avg_squad_value = []
    league_two_avg_squad_value = []
    #print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 2003: #don't take into account years that don't have values
            if row['League level'] == 'First Tier':
                premier_league_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
            elif row['League level'] == 'Second Tier':
                championship_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
            elif row['League level'] == 'Third Tier':
                league_one_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
            elif row['League level'] == 'Fourth Tier':
                league_two_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_avg_squad_value)
    championship_median, championship_avg = errors.median_avg_errors(championship_avg_squad_value)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_avg_squad_value)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_avg_squad_value)

    data = append_values_to_data(team, premier_league_median, premier_league_avg, championship_median, championship_avg,
                                 league_one_median, league_one_avg, league_two_median, league_two_avg)

    file_handling.calculations_to_csv("all_values.csv", "Inflation adjusted average squad value M€", data)

def attendances_by_league_level(team):
    team_df = values_for_analysis.league_tier_throughout_years(team)

    #print(values_for_analysis.league_tier_throughout_years(team))

    premier_league_spectators = []
    championship_spectators = []
    league_one_spectators = []
    league_two_spectators = []

    #print(f'\n{team}')
    for index, row in team_df.iterrows():
        if row['Year'] > 1995 and row['Year'] != 2020: #don't take into account years that don't have values and COVID year without spectators
            if row['League level'] == 'First Tier':
                premier_league_spectators.append(row['Total spectators'])
            elif row['League level'] == 'Second Tier':
                championship_spectators.append(row['Total spectators'])
            elif row['League level'] == 'Third Tier':
                league_one_spectators.append(row['Total spectators'])
            elif row['League level'] == 'Fourth Tier':
                league_two_spectators.append(row['Total spectators'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_spectators)
    championship_median, championship_avg = errors.median_avg_errors(championship_spectators)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_spectators)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_spectators)

    data = append_values_to_data(team, premier_league_median, premier_league_avg, championship_median, championship_avg,
                                 league_one_median, league_one_avg, league_two_median, league_two_avg)

    print(data)


def append_values_to_data(team, premier_league_median, premier_league_avg, championship_median, championship_avg, league_one_median, league_one_avg, league_two_median, league_two_avg):
    data = []

    if team != 'Total':
        data.append(team)
    data.append(premier_league_median)
    data.append(premier_league_avg)

    data.append(championship_median)
    data.append(championship_avg)

    data.append(league_one_median)
    data.append(league_one_avg)

    data.append(league_two_median)
    data.append(league_two_avg)

    return data

def calculate_pearson_correlation_coefficient(x_values, y_values):
    covariance = np.cov(x_values, y_values)[0][1]
    stdev_x = statistics.stdev(x_values)
    stdev_y = statistics.stdev(y_values)
    pearson_correlation_coefficient = round(covariance / (stdev_x * stdev_y), 8)

    return pearson_correlation_coefficient


def calculate_r_squared(slope, intercept, x_values, y_values):
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    predicted_values = slope * x_values + intercept
    residuals = y_values - predicted_values
    ssr = np.sum(residuals ** 2)
    mean_value = statistics.mean(y_values)
    sst = np.sum((y_values - mean_value) ** 2)
    r_squared = round(1 - (ssr / sst), 2)

    n = len(y_values)
    p = 1
    adjusted_r_squared = 1 - ((1 - r_squared) * (n - 1) / (n - p - 1))

    return r_squared, round(adjusted_r_squared, 2)

def calculate_mse_rmse_mae(slope, intercept, x_values, y_values):
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    predicted_values = slope * x_values + intercept
    residuals = y_values - predicted_values

    mse = np.mean(residuals ** 2)
    rmse = round(np.sqrt(mse), 2)
    mae = round(np.mean(np.abs(residuals)), 2)

    return round(mse, 2), rmse, mae
