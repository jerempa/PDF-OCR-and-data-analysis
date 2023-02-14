import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


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
            if key == 'turnover':
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
    #print(turnover, years)
    #print(turnover2)
    #plt.scatter(years, turnover)
    fig, ax = plt.subplots()
    ax.scatter(years, turnover)

    # Format the y-axis labels
    def format_func(value1, tick_number):
        return "{:,}".format(value1)

    formatter = ticker.FuncFormatter(format_func)
    ax.yaxis.set_major_formatter(formatter)
    plt.xlabel("Year")
    plt.ylabel("Turnover")
    plt.title("Turnover over 20 years")
    plt.show()
