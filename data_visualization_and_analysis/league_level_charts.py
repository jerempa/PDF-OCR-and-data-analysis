import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

from data_fetchers import df_operations
from data_visualization_and_analysis import values_for_analysis

#teams = ['Brighton & Hove Albion', 'Leeds United', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Queens Park Rangers', 'Ipswich Town']
teams = ['Brighton & Hove Albion', 'Leeds United']
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
#seasons = ['22/23', '21/22', '20/21', '19/20', '18/19', '17/18', '16/17', '15/16', '14/15', '13/14', '12/13', '11/12', '10/11', '09/10', '08/09', '07/08', '06/07', '05/06', '04/05', '03/04', '02/03', '01/02', '00/01', '99/00']
color_map = {'First Tier': 'green', 'Second Tier': 'yellow', 'Third Tier': 'red', None: 'white'}
background_color = {
    'First Tier': '#C5E5A5',
    'Second Tier': '#FFF2CC',
    'Third Tier': '#FFC7CE'
}

def line_plot():
    attendances = []
    #fig, ax = plt.subplots()
    #ax.set_xlim(2000, 2022)
    #ax.set_ylim(0, 50000)

    for team in teams:

        df = values_for_analysis.league_tier_throughout_years(team)
        #print(df)
        y_axis_values = ['Average attendance', 'Arrivals', 'Squad market value', 'Average squad market value']
        #print(df['Arrivals'].max())
        #y_axis_values = {'Average attendance'}


        for value in y_axis_values:
            fig, ax = plt.subplots()
            for level in df['League level'].unique():
                level_df = df[df['League level'] == level]
                start_year = level_df['Year'].min()
                end_year = level_df['Year'].max()
                ax.axvspan(start_year - 0.5, end_year + 0.5, facecolor=background_color[level], alpha=0.5)

            df.plot(x='Year', y=value, ax=ax, color='black')
            ax.set_xlim(2000, 2025)
            ax.set_ylim(0, df[value].max() + df[value].max() / 10)

            plt.title(f'{team} {value} by season')
            plt.xlabel('Year')
            plt.ylabel(value)

            plt.show()

        bar_chart(df)

def bar_chart(df):
    bar_width = 0.8
    opacity = 0.8

    fig, ax = plt.subplots()

    ax.set_facecolor('white')
    for tier in df['League level'].unique():
        df_tier = df[df['League level'] == tier]
        ax.bar(df_tier['Year'], df_tier['Average attendance / capacity %'], bar_width, alpha=opacity, color=color_map[tier], label=tier)

    ax.set_title('Average Attendance / Capacity % by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Attendance / Capacity %')

    ax.legend()

    plt.show()




