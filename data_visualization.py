import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def scatter_chart(data):
    turnover = []
    turnover2 = []
    years = []
    #print(data)
    data = data['Brighton']
    #print(data)
    for year, year_data in data.items():
        #print(year, year_data)
        for key, value in year_data.items():
            if key == 'turnover' or key == 'revenue':
                turnover2.append(value)
                value = value.replace(',', '')
                try:
                    value = int(value)
                    if len(str(value)) == 5 or len(str(value)) == 6:
                        value *= 1000
                    turnover.append(value)
                    years.append(year)
                except ValueError:
                    pass
    fig, ax = plt.subplots()
    ax.set_ylim(0, 155000000)
    ax.set_xlim(1999, 2022)

    red_threshold = [1999, 2011.5]
    orange_threshold = [2011.5, 2017.5]
    green_threshold = [2017.5, 2022]
    color1 = '#FF4136'  #red
    color2 = '#FF851B'  #orange
    color3 = '#2ECC40'  #green

    ax.plot(years, turnover, color='blue')

    ax.axvspan(red_threshold[0], red_threshold[1], color=color1, alpha=0.2)
    ax.axvspan(orange_threshold[0], orange_threshold[1], color=color2, alpha=0.2)
    ax.axvspan(green_threshold[0], green_threshold[1], color=color3, alpha=0.2)

    def format_func(value1, tick_number):
        return "{:,}".format(value1)

    formatter = ticker.FuncFormatter(format_func)
    ax.yaxis.set_major_formatter(formatter)
    plt.xlabel("Year")
    plt.ylabel("Turnover")
    plt.title("Turnover over 20 years")

    #ax.set_facecolor('white')
    plt.show()
