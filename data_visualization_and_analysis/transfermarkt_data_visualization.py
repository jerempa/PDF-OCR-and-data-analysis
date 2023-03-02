import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import statistics

from data_fetchers import df_operations
from data_visualization_and_analysis import values_for_analysis
from file_operations import file_handling
from error_handling import errors
#https://matplotlib.org/stable/gallery/color/named_colors.html

#teams = ['Brighton & Hove Albion', 'Leeds United', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Queens Park Rangers', 'Ipswich Town']
#teams = ['Leeds United']
teams = ['Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
         'Blackburn Rovers', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Queens Park Rangers', 'Wigan Athletic',
         'Bolton Wanderers', 'Charlton Athletic', 'Derby County', 'Ipswich Town', 'Portsmouth FC']
#seasons = ['22/23', '21/22', '20/21', '19/20', '18/19', '17/18', '16/17', '15/16', '14/15', '13/14', '12/13', '11/12', '10/11', '09/10', '08/09', '07/08', '06/07', '05/06', '04/05', '03/04', '02/03', '01/02', '00/01', '99/00']
color_map = {'First Tier': 'green', 'Second Tier': 'yellow', 'Third Tier': 'orange', 'Fourth Tier': 'red', None: 'white'}
background_color = {
    'First Tier': '#C5E5A5',
    'Second Tier': '#FFF2CC',
    'Third Tier': '#FFC7CE',
    'Fourth Tier': 'orange'
}

#league_levels = ['Premier League', 'Championship', 'League One', 'League Two']
y_axis_headers = ["Average attendance / capacity %", "Inflation adjusted arrivals", "Inflation adjusted squad value", "Inflation adjusted average squad value"]

def scatter_chart():
    for header in y_axis_headers:
        for team in teams:
            league_levels = [1, 2, 3, 4]
            values = values_for_analysis.league_tier_throughout_years(team)

            print(team, values)
            # values = file_handling.return_transfermarkt_values_from_csv(team, header)
            # #ax.set_xlim(2000, 2022)
            # #ax.set_ylim(0, 50000)
            # if None in values:
            #     index = values.index(None)
            #     values.remove(None)
            #     league_levels.pop(index)
            # if None not in values:
            #     slope, intercept = np.polyfit(league_levels, values, 1)
            #     covariance = np.cov(league_levels, values)[0][1]
            #     stdev_x = statistics.stdev(league_levels)
            #     stdev_y = statistics.stdev(values)
            #     pearson_correlation_coefficient = round(covariance/(stdev_x * stdev_y), 8)
            #     #print(team, header, pearson_correlation_coefficient)
            #     #print(round(slope, 2), round(intercept, 2), team)
            #     #file_handling.calculations_to_csv("regression_results.csv", header, [team, pearson_correlation_coefficient])
            #
            #     plt.plot(league_levels, slope * np.array(league_levels) + intercept, color='red')
            #
            #
            # plt.scatter(league_levels, values)
            #
            #
            #
            # plt.xlabel('League Level')
            # plt.ylabel(header)
            # plt.title(f'Regression analysis league level and {header}')

            #plt.show()





#