import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

from data_fetchers import df_operations

teams = ['Blackpool FC', 'Brighton', 'Huddersfield', 'Hull', 'Ipswich Town', 'Leeds', 'QPR']

def scatter_chart(data):
    turnover = []
    turnover2 = []
    years = []
    #print(data)
    #data = data['Hull']
    #print(data)
    for team in teams:
        #print(team, type(team))
        curr_team = data[team]
        for year, year_data in curr_team.items():
            # #print(team, team_data)
            # for year, year_data in team_data.items():
            #     #print(year_data)
            #     for key, value in year_data:
            #         print(kye, value)
            #         if key == 'turnover' or key == 'revenue:':
            #             turnover2.append(value)
            #             value = value.replace(',', '')
            #             try:
            #                 value = int(value)
            #                 if len(str(value)) == 4 or len(str(value)) == 5 or len(str(value)) == 6:
            #                     value *= 1000
            #                 turnover.append(value)
            #                 years.append(year)
            #             except ValueError:
            #                 pass
            for key, value in year_data.items():
                if key == 'turnover' or key == 'revenue':
                    turnover2.append(value)
                    value = value.replace(',', '')
                    try:
                        value = int(value)
                        if len(str(value)) == 4 or len(str(value)) == 5 or len(str(value)) == 6:
                            value *= 1000
                        turnover.append(value)
                        years.append(year)
                    except ValueError:
                        pass
    print(turnover, len(turnover))
    print(turnover2, len(turnover2))
    print(years)
    league_tier = [None] * len(turnover)
    # k = 0
    # j = 43
    # r = 86
    #value = len(turnover) / 68 #teams in BPL, champ and League One
    for index, i in enumerate(turnover):
        #print(index)
        if i <= 20000000:
            league_tier[index] = 1
        elif i <= 50000000:
            league_tier[index] = 2
        else:
            league_tier[index] = 3

    print(len(years), len(league_tier), league_tier)
    #turnover[9] = int(11075152)
    fig, ax = plt.subplots()
    # ax.set_ylim(0, 150000000)
    # ax.set_xlim(1, 3)
    ax.set_xlim(0, 150000000)
    ax.set_ylim(1, 3)
    # ax.set_xlim(0, 200000000)
    # ax.set_ylim(1, 3)

    m, b = np.polyfit(league_tier, turnover, 1)
    line_x = np.arange(1, len(league_tier))
    line_y = m * line_x + b
    plt.plot(line_x, line_y, color='red')

    # red_threshold = [1999, 2011.5]
    # orange_threshold = [2011.5, 2017.5]
    # green_threshold = [2017.5, 2022] #brighton
    # red_threshold = [2002.5, 2004]
    # orange_threshold1 = [2004, 2011]
    # orange_threshold2 = [2013, 2014]
    # orange_threshold3 = [2015, 2022]
    # green_threshold1 = [2011, 2013]
    # green_threshold2 = [2014, 2015] #QPR
    # color1 = '#FF4136'  #red
    # color2 = '#FF851B'  #orange
    # color3 = '#2ECC40'  #green
    #
    #
    #
    # ax.axvspan(red_threshold[0], red_threshold[1], color=color1, alpha=0.2)
    # ax.axvspan(orange_threshold1[0], orange_threshold1[1], color=color2, alpha=0.2)
    # ax.axvspan(orange_threshold2[0], orange_threshold2[1], color=color2, alpha=0.2)
    # ax.axvspan(orange_threshold3[0], orange_threshold3[1], color=color2, alpha=0.2)
    # ax.axvspan(green_threshold1[0], green_threshold1[1], color=color3, alpha=0.2)
    # ax.axvspan(green_threshold2[0], green_threshold2[1], color=color3, alpha=0.2)
    #thresholds = [(2002.5, 2004), (2004, 2011), (2011, 2013), (2013, 2014), (2014, 2015), (2015, 2022)] #qpr
    thresholds = [(2002.5, 2004.5), (2004.5, 2008.5), (2008.5, 2010.5), (2010.5, 2013.5), (2013.5, 2015.5), (2015.5, 2016.5), (2016.5, 2017.5), (2017.5, 2018.5), (2018.5, 2020.5), (2020.5, 2021)] #hull
    # colors = ['#FF4136', '#FF851B', '#2ECC40', '#FF851B', '#2ECC40', '#FF851B', '#2ECC40', '#FF851B', '#FF851B', '#FF4136'] # hull
    #
    # for i, (t1, t2) in enumerate(thresholds):
    #     ax.axvspan(t1, t2, color=colors[i], alpha=0.2)

    #ax.scatter(years, turnover, color='blue')
    ax.scatter(turnover, league_tier, color='blue')


    def format_func(value1, tick_number):
        return "{:,}".format(value1)

    formatter = ticker.FuncFormatter(format_func)
    ax.yaxis.set_major_formatter(formatter)
    plt.xlabel("League tier")
    plt.ylabel("Turnover")
    plt.title("Correlation between league tier and revenue")

    #ax.set_facecolor('white')
    plt.show()
