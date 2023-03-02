import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import statistics

from data_fetchers import df_operations
from data_visualization_and_analysis import values_for_analysis
from file_operations import file_handling
from data_visualization_and_analysis import calculations
#https://matplotlib.org/stable/gallery/color/named_colors.html

#teams = ['Brighton & Hove Albion', 'Leeds United', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Queens Park Rangers', 'Ipswich Town']
# teams = ['Leeds United']
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
#y_axis_headers = ["Average attendance / capacity %"]
y_axis_headers = ["Average attendance / capacity %", "Infl adjusted arrivals M€", "Infl adjusted squad market value M€", "Infl adjusted avg squad market value M€"]


def scatter_chart():
    for header in y_axis_headers:
        for team in teams:
            #league_levels = [1, 2, 3, 4]
            df = values_for_analysis.league_tier_throughout_years(team)

            league_pos = df['Position'].tolist()
            values = df[header].tolist()


            if header == "Infl adjusted squad market value M€" or header == "Infl adjusted avg squad market value M€":
                league_pos = league_pos[:19]
                values = values[:19] #ignore the none values that appear 1999-2004

            #if header == "Average attendance / capacity %":
            values.pop(2) #ignore COVID season
            league_pos.pop(2)
            #values = file_handling.return_transfermarkt_values_from_csv(team, header)

            #ax.set_xlim(2000, 2022)
            #ax.set_ylim(0, 50000)

            slope, intercept = np.polyfit(league_pos, values, 1)
            # covariance = np.cov(league_pos, values)[0][1]
            # stdev_x = statistics.stdev(league_pos)
            # stdev_y = statistics.stdev(values)
            # pearson_correlation_coefficient = round(covariance/(stdev_x * stdev_y), 8)
            pearson_correlation_coefficient = calculations.calculate_pearson_correlation_coefficient(league_pos, values)

            r_squared = calculations.calculate_r_squared(slope, intercept, league_pos, values)


            file_handling.calculations_to_csv("regression_results_without_covid_season.csv", header, [team, pearson_correlation_coefficient, r_squared])

            plt.plot(league_pos, slope * np.array(league_pos) + intercept, color='red')


            plt.scatter(league_pos, values)



            plt.xlabel('League position')
            plt.ylabel(header)
            plt.title(f'Regression analysis league level & position and {header} {team}')

            #plt.show()



