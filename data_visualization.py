import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def scatter_chart(data):
    turnover = []
    turnover2 = []
    years = []
    #print(data)
    data = data['QPR']
    print(data)
    for year, year_data in data.items():
        #print(year, year_data)
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
    fig, ax = plt.subplots()
    ax.set_ylim(0, 155000000)
    ax.set_xlim(2002, 2022)

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
    thresholds = [(2002.5, 2004), (2004, 2011), (2011, 2013), (2013, 2014), (2014, 2015), (2015, 2022)]
    colors = ['#FF4136', '#FF851B', '#2ECC40', '#FF851B', '#2ECC40', '#FF851B']

    for i, (t1, t2) in enumerate(thresholds):
        ax.axvspan(t1, t2, color=colors[i], alpha=0.2)

    ax.plot(years, turnover, color='blue')

    def format_func(value1, tick_number):
        return "{:,}".format(value1)

    formatter = ticker.FuncFormatter(format_func)
    ax.yaxis.set_major_formatter(formatter)
    plt.xlabel("Year")
    plt.ylabel("Turnover")
    plt.title("Turnover over 20 years")

    #ax.set_facecolor('white')
    plt.show()
