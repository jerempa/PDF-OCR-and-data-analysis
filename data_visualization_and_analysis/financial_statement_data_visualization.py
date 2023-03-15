import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import statistics

from data_fetchers import df_operations
from data_visualization_and_analysis import values_for_analysis
from file_operations import file_handling
from data_visualization_and_analysis import calculations
#https://matplotlib.org/stable/gallery/color/named_colors.html
#Bournemouth 7 and Third Tier

position_98_99_season = {'Brentford FC': [1, "Fourth Tier"], 'Brighton & Hove Albion': [17, "Fourth Tier"], 'Leeds United': [4, "First Tier"], 'Leicester City': [10, "First Tier"], 'Nottingham Forest': [20, "First Tier"], 'Southampton FC': [17, "First Tier"], 'Wolverhampton Wanderers': [7, "Second Tier"],
         'Blackburn Rovers': [19, "First Tier"], 'Blackpool FC': [14, "Third Tier"], 'Huddersfield Town': [10, "Second Tier"], 'Hull City': [21, "Fourth Tier"], 'Norwich City': [9, "Second Tier"], 'Sunderland AFC': [1, "Second Tier"], 'Swansea City': [7, "Fourth Tier"], 'Queens Park Rangers': [20, "Second Tier"], 'Wigan Athletic': [6, "Third Tier"],
         'Bolton Wanderers': [6, "Second Tier"], 'Charlton Athletic': [18, "First Tier"], 'Ipswich Town': [3, "Second Tier"], 'Portsmouth FC': [19, "Second Tier"]}

#teams = ['Brighton & Hove Albion', 'Leeds United', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Queens Park Rangers', 'Ipswich Town']
#teams = ['Leicester City']
teams = ['Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
         'Blackburn Rovers', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Sunderland AFC', 'Swansea City', 'Queens Park Rangers', 'Wigan Athletic',
         'Bolton Wanderers', 'Charlton Athletic', 'Ipswich Town', 'Portsmouth FC']
#seasons = ['22/23', '21/22', '20/21', '19/20', '18/19', '17/18', '16/17', '15/16', '14/15', '13/14', '12/13', '11/12', '10/11', '09/10', '08/09', '07/08', '06/07', '05/06', '04/05', '03/04', '02/03', '01/02', '00/01', '99/00']
color_map = {'First Tier': 'green', 'Second Tier': 'yellow', 'Third Tier': 'orange', 'Fourth Tier': 'red', None: 'white'}
background_color = {
    'First Tier': '#C5E5A5',
    'Second Tier': '#FFF2CC',
    'Third Tier': '#FFC7CE',
    'Fourth Tier': 'orange'
}

#league_levels = ['Premier League', 'Championship', 'League One', 'League Two']
#y_axis_headers = ["Average attendance"]
y_axis_headers = ["turnover", "inflation adjusted wages (in thousands)", "assets (in thousands)", "debt (in thousands)", "result for the financial year"]


def scatter_chart():
    teams.sort()
    #print(teams)
    for header in y_axis_headers:
        for team in teams:
            df = values_for_analysis.financial_statement_data_cleansing(team)

            #print(team, df)
            league_pos = df['position'].tolist()
            for key, data in position_98_99_season.items():
                if key == team:
                    pos_98 = values_for_analysis.calculate_position(data[0], data[1])
                    league_pos[0] = pos_98 #calculate position for 98_99 season for y-axis

            values = df[header].tolist()

            #print(league_pos)

            # values.pop(2) #ignore COVID season
            # league_pos.pop(2)


            #ax.set_xlim(2000, 2022)
            #ax.set_ylim(0, 50000)

            slope, intercept = np.polyfit(league_pos, values, 1)
            #pearson_correlation_coefficient = calculations.calculate_pearson_correlation_coefficient(league_pos, values)

            correlation_calculations = calculations.calculate_pearson_correlation_coefficient(league_pos,
                                                                                              values)

            pearson_correlation_coefficient = correlation_calculations[0]
            covariance = correlation_calculations[1]
            stdev_x = correlation_calculations[2]
            stdev_y = correlation_calculations[3]

            r_calculations = calculations.calculate_r_squared(slope, intercept, league_pos, values)

            r_squared = r_calculations[0]
            adjusted_r_squared = r_calculations[1]

            error_calculations = calculations.calculate_mse_rmse_mae(slope, intercept, league_pos, values)

            mean_squared_error = error_calculations[0]
            root_mean_squared_error = error_calculations[1]
            mean_absolute_error = error_calculations[2]

            n = len(values)


            # file_handling.calculations_to_csv("financial_statement_regression_results3.csv", header, [team, n, covariance, stdev_x, stdev_y,
            #                                                                                            pearson_correlation_coefficient, r_squared, adjusted_r_squared, mean_squared_error,
            #                                                                                            root_mean_squared_error, mean_absolute_error])

            plt.plot(league_pos, slope * np.array(league_pos) + intercept, color='red')


            plt.scatter(league_pos, values)



            plt.xlabel('League position')
            plt.ylabel(header)
            plt.title(f'Regression analysis league position and {header} {team}')

            #plt.show()
        # scatter_chart_for_all_values(header)


def scatter_chart_for_all_values(header):
    teams.sort()
    #for header in y_axis_headers:
    total_positions = []
    total_values = []
    for team in teams:
        df = values_for_analysis.financial_statement_data_cleansing(team)

        league_pos = df['position'].tolist()
        for key, data in position_98_99_season.items():
            if key == team:
                pos_98 = values_for_analysis.calculate_position(data[0], data[1])
                league_pos[0] = pos_98 #calculate position for 98_99 season for y-axis

        values = df[header].tolist()



         # values.pop(2) #ignore COVID season
        # league_pos.pop(2)
        #values = file_handling.return_transfermarkt_values_from_csv(team, header)


        #ax.set_xlim(2000, 2022)
        #ax.set_ylim(0, 50000)
        for i in league_pos:
            total_positions.append(i)
        for j in values:
            total_values.append(j)
    slope, intercept = np.polyfit(total_positions, total_values, 1)
    correlation_calculations = calculations.calculate_pearson_correlation_coefficient(total_positions, total_values)

    pearson_correlation_coefficient = correlation_calculations[0]
    covariance = correlation_calculations[1]
    stdev_x = correlation_calculations[2]
    stdev_y = correlation_calculations[3]


    r_calculations = calculations.calculate_r_squared(slope, intercept, total_positions, total_values)

    r_squared = r_calculations[0]
    adjusted_r_squared = r_calculations[1]

    error_calculations = calculations.calculate_mse_rmse_mae(slope, intercept, total_positions, total_values)

    mean_squared_error = error_calculations[0]
    root_mean_squared_error = error_calculations[1]
    mean_absolute_error = error_calculations[2]
    n = len(total_values)


    file_handling.calculations_to_csv("financial_statement_regression_results3.csv", header, ["Total", n, covariance, stdev_x, stdev_y, pearson_correlation_coefficient,
                                                                                               r_squared, adjusted_r_squared, mean_squared_error, root_mean_squared_error, mean_absolute_error])

    plt.plot(total_positions, slope * np.array(total_positions) + intercept, color='red')


    plt.scatter(total_positions, total_values)



    plt.xlabel('League position')
    plt.ylabel(header)
    plt.title(f'Regression analysis league level & position and {header} all clubs')

    #plt.show()

def line_plot_and_color_visualization():

    for header in y_axis_headers:

        for team in teams:

            df = values_for_analysis.transfermarkt_data_cleansing(team)
            years = df['Year'].astype(int).tolist()
            values = df[header].tolist()

            fig, ax = plt.subplots()

            if header == "Infl adjusted squad market value M€" or header == "Infl adjusted avg squad market value M€":
                years = years[:19]
                values = values[:19] #ignore the none values that appear 1999-2004

            values.pop(2) #ignore COVID season
            years.pop(2)

            slope, intercept = np.polyfit(years, values, 1)

            plt.plot(years, slope * np.array(years) + intercept, color='red')

            for level in df['League level'].unique():
                level_df = df[df['League level'] == level]
                start_year = level_df['Year'].min()
                end_year = level_df['Year'].max()
                ax.axvspan(start_year - 0.5, end_year + 0.5, facecolor=background_color[level], alpha=0.5)

            handles = [plt.Rectangle((0, 0), 1, 1, color=background_color[level], alpha=0.5) for level in
                       background_color]

            labels = list(background_color.keys())
            ax.legend(handles, labels)

            ax.set_xlim(2000, 2022)
            ax.set_ylim(0, max(values) + (max(values) / 10))

            plt.plot(years, values)

            plt.title(f'{team} {header} by season')
            plt.xlabel('Year')
            plt.ylabel(header)

            plt.show()

            bar_chart(df, team)


def bar_chart(df, team):
    bar_width = 0.8
    opacity = 0.8

    fig, ax = plt.subplots()

    ax.set_xlim(1998.5, 2022.5)

    ax.set_facecolor('white')
    for tier in df['League level'].unique():
        df_tier = df[df['League level'] == tier]
        ax.bar(df_tier['Year'], df_tier['Average attendance / capacity %'], bar_width, alpha=opacity, color=color_map[tier], label=tier)

    ax.set_title(f'{team} Average Attendance / Capacity % by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Attendance / Capacity %')

    ax.legend()

    plt.show()




