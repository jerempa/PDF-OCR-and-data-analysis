import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

from data_fetchers import df_operations
from data_visualization_and_analysis import values_for_analysis
from file_operations import file_handling
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
league_levels = [1, 2, 3, 4]
y_axis_values = ["Average attendance / capacity %", "Inflation adjusted arrivals", "Inflation adjusted squad value", "Inflation adjusted average squad value"]

def scatter_chart():
    for team in teams:
        for value in y_axis_values:
            values = file_handling.return_transfermarkt_values_from_csv(team, value)
            #ax.set_xlim(2000, 2022)
            #ax.set_ylim(0, 50000)
            slope, intercept = np.polyfit(league_levels, values, 1)

            plt.scatter(league_levels, values)

            plt.plot(league_levels, slope * np.array(league_levels) + intercept, color='red')

            plt.xlabel('League Level')
            plt.ylabel(value)
            plt.title(f'Regression analysis league level and {value}')

            plt.show()





