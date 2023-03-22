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
#teams = ['AFC Bournemouth']
teams = ['AFC Bournemouth', 'Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
         'Blackburn Rovers', 'Blackpool FC', 'Cardiff City', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Reading FC', 'Sheffield United', 'Stoke City', 'Sunderland AFC', 'Swansea City', 'Queens Park Rangers', 'Wigan Athletic',
         'Bolton Wanderers', 'Charlton Athletic', 'Derby County', 'Ipswich Town', 'Portsmouth FC'] #26 kpl
#seasons = ['22/23', '21/22', '20/21', '19/20', '18/19', '17/18', '16/17', '15/16', '14/15', '13/14', '12/13', '11/12', '10/11', '09/10', '08/09', '07/08', '06/07', '05/06', '04/05', '03/04', '02/03', '01/02', '00/01', '99/00']
color_map = {'First Tier': 'green', 'Second Tier': 'yellow', 'Third Tier': 'orange', 'Fourth Tier': 'red', None: 'white'}
background_color = {
    'First Tier': '#C5E5A5',
    'Second Tier': '#FFF2CC',
    'Third Tier': '#FFC7CE',
    'Fourth Tier': 'orange'
}

#league_levels = ['Premier League', 'Championship', 'League One', 'League Two']
y_axis_headers = ["Ln(Infl adjusted avg squad market value M€)"]
#y_axis_headers = ["Average attendance", "Average attendance / capacity %", "Infl adjusted arrivals M€", Ln("Infl adjusted squad market value M€)", "Infl adjusted avg squad market value M€"]


def scatter_chart():
    teams.sort()
    #print(teams)
    for header in y_axis_headers:
        for team in teams:
            #league_levels = [1, 2, 3, 4]
            df = values_for_analysis.transfermarkt_data_cleansing(team)
            #print(team, df)

            league_pos = df['Position'].tolist()
            y_values = df[header].tolist()
            x_2 = df['Stadium capacity'].tolist()
            x_3 = df['City population'].tolist()
            #x_4 = df['(Distance to the nearest major city (km))^2'].tolist()
            x_4 = df['Distance to the nearest major city (km)'].tolist()
            x_5 = df['(Squad size)^2'].tolist()
            x_6 = df['Managerial change'].tolist()
            x_7 = df['(Average squad age (years))^2'].tolist()


            #print(f'{league_pos}{len(league_pos)} x_1\n{x_2}{len(x_2)}x_2\n{y_values}{len(y_values)}\n{team, header}\n')

            #if header == "Infl adjusted squad market value M€" or header == "Infl adjusted avg squad market value M€":
            league_pos = league_pos[1:19]
            y_values = y_values[1:19] #ignore the none values that appear 1999-2004
            x_2 = x_2[1:19]
            x_3 = x_3[1:19]
            x_4 = x_4[1:19]
            x_5 = x_5[1:19]
            x_6 = x_6[1:19]
            x_7 = x_7[1:19]
            y_values.pop(2) #ignore COVID season
            league_pos.pop(2)
            x_2.pop(2)
            x_3.pop(2)
            x_4.pop(2)
            x_5.pop(2)
            x_6.pop(2)
            x_7.pop(2)
            # else:
            #     league_pos = league_pos[1:22]
            #     y_values = y_values[1:22] #ignore the none values that appear 1999-2004
            #     x_2 = x_2[1:22]
            #     x_3 = x_3[1:22]
            #     x_4 = x_4[1:22]
            #     x_5 = x_5[1:22]
            #     x_6 = x_6[1:22]
            #     x_7 = x_7[1:22]
            #
            #     y_values.pop(1) #ignore COVID season
            #     league_pos.pop(1)
            #     x_2.pop(1)
            #     x_3.pop(1)
            #     x_4.pop(1)
            #     x_5.pop(1)
            #     x_6.pop(1)
            #     x_7.pop(1)
            #
            # print(league_pos)
            # print(x_2)
            # print(x_3)
            # print(x_4)
            # print(x_5)
            # print(x_6)
            # print(x_7)
            # print(y_values)


            #if header == "Average attendance / capacity %":
            # y_values.pop(2) #ignore COVID season
            # league_pos.pop(2)
            # x_2.pop(2)
            # x_3.pop(2)
            # x_4.pop(2)
            # x_5.pop(2)
            # x_6.pop(2)
            # x_7.pop(2)

            #print(f'{league_pos}{len(league_pos)} x_1\n{x_2}{len(x_2)}x_2\n{y_values}{len(y_values)}\n{team, header}\n')


            # if header == 'Total spectators':
            #     values.pop(0)
            #     league_pos.pop(0) #ignore the latest season for total spectators as the value isn't comparable to other seasons

            #ax.set_xlim(2000, 2022)
            #ax.set_ylim(0, 50000)

            #slope, intercept = np.polyfit(league_pos, values, 1)
            #pearson_correlation_coefficient = calculations.calculate_pearson_correlation_coefficient(league_pos, values)

            # correlation_calculations = calculations.calculate_pearson_correlation_coefficient(league_pos,
            #                                                                                   values)
            #
            # pearson_correlation_coefficient = correlation_calculations[0]
            # covariance = correlation_calculations[1]
            # stdev_x = correlation_calculations[2]
            # stdev_y = correlation_calculations[3]
            #
            # r_calculations = calculations.calculate_r_squared(league_pos, x_2, y_values)
            #
            # r_squared = r_calculations[0]
            # adjusted_r_squared = r_calculations[1]

            #regression_calculations = calculations.regression_calcs(league_pos, x_2, x_3, x_4, x_5, x_6, x_7, y_values)
            #
            #
            # intercept_coefficient = regression_calculations[0][0]
            # x_1_coefficient = regression_calculations[0][1]
            # x_2_coefficient = regression_calculations[0][2]
            # x_3_coefficient = regression_calculations[0][3]
            #
            #
            # intercept_p_value = round(float(regression_calculations[1][0]), 10)
            # x_1_p_value = round(float(regression_calculations[1][1]), 10)
            # x_2_p_value = round(float(regression_calculations[1][2]), 10)
            # x_3_p_value = round(float(regression_calculations[1][3]), 10)
            #
            # intercept_std_err = regression_calculations[2][0]
            # x_1_std_err = regression_calculations[2][1]
            # x_2_std_err = regression_calculations[2][2]
            # x_3_std_err = regression_calculations[2][3]
            #
            #
            # intercept_t_value = round(float(regression_calculations[3][0]), 10)
            # x_1_t_value = round(float(regression_calculations[3][1]), 10)
            # x_2_t_value = round(float(regression_calculations[3][2]), 10)
            # x_3_t_value = round(float(regression_calculations[3][3]), 10)
            #
            # r_squared = regression_calculations[4]
            # adjusted_r_squared = regression_calculations[5]

            #print(x_1_coefficient, x_1_p_value, x_1_std_err)
            #
            # error_calculations = calculations.calculate_mse_rmse_mae(slope, intercept, league_pos, values)
            #
            # mean_squared_error = error_calculations[0]
            # root_mean_squared_error = error_calculations[1]
            # mean_absolute_error = error_calculations[2]
            #
            n = len(y_values)
            # file_handling.calculations_to_csv("regression_results_without_covid_season11.csv", header, [team, n, intercept_coefficient, x_1_coefficient, x_2_coefficient,
            #                                                                                             intercept_t_value, x_1_t_value, x_2_t_value,
            #                                                                                            intercept_p_value, x_1_p_value, x_2_p_value,
            #                                                                                             intercept_std_err, x_1_std_err, x_2_std_err,
            #                                                                                             r_squared, adjusted_r_squared])


            # file_handling.calculations_to_csv("regression_results_without_covid_season9.csv", header, [team, n, covariance, stdev_x, stdev_y,
            #                                                                                            pearson_correlation_coefficient, r_squared, adjusted_r_squared, mean_squared_error,
            #                                                                                            root_mean_squared_error, mean_absolute_error])


            #plt.plot(league_pos, slope * np.array(league_pos) + intercept, color='red')


            #plt.scatter(league_pos, values)



            plt.xlabel('League position')
            plt.ylabel(header)
            plt.title(f'Regression analysis league level & position and {header} {team}')

            #plt.show()
        scatter_chart_for_all_values(header)


def scatter_chart_for_all_values(header):
    teams.sort()
    # for header in y_axis_headers:
    total_positions = []
    total_values = []
    x_2_total = []
    x_3_total = []
    x_4_total = []
    x_5_total = []
    x_6_total = []
    x_7_total = []
    x_8_total = []
    x_9_total = []
    for team in teams:
        #league_levels = [1, 2, 3, 4]
        df = values_for_analysis.transfermarkt_data_cleansing(team)

        league_pos = df['Position'].tolist()
        y_values = df[header].tolist()
        #avg attendance and avg attendance / capacity predictors:
        #x_2 = df['Stadium capacity'].tolist()
        # x_2 = df['Stadium capacity (thousands)'].tolist()
        # #x_3 = df['City population'].tolist()
        # x_3 = df['Ln(City population)'].tolist()
        # x_4 = df['Distance to the nearest major city (km)'].tolist()
        # x_5 = df['City has a professional rugby team'].tolist()
        # x_6 = df['Only football team in top 4 leagues in the metropolitan county'].tolist()
        # x_7 = df['Team is in the Premier League'].tolist()

        #squad market value and avg squad market value predictors:
        x_2 = df['(Squad size)^2'].tolist()
        x_3 = df['(Average squad age (years))^2'].tolist()
        x_4 = df['Team is in the Premier League'].tolist()



        #Arrivals:
        # x_2 = df['(Average squad age (years))^2'].tolist()
        # x_3 = df['Managerial change'].tolist()
        # x_4 = df['Team is in the Premier League'].tolist()

        #print(y_values)
        #print(team, df)





        # if header == "Infl adjusted squad market value M€" or header == "Infl adjusted avg squad market value M€":
        #     league_pos = league_pos[:19]
        #     y_values = y_values[:19] #ignore the none values that appear 1999-2004
        #     x_2 = x_2[:19]
        #
        #print(x_2)
        # #if header == "Average attendance / capacity %":
        # y_values.pop(2) #ignore COVID season
        # league_pos.pop(2)
        # x_2.pop(2)
        league_pos = league_pos[1:19]
        y_values = y_values[1:19]  # ignore the none values that appear 1999-2004
        x_2 = x_2[1:19]
        x_3 = x_3[1:19]
        x_4 = x_4[1:19]
        # x_5 = x_5[1:19]
        # x_6 = x_6[1:19]
        # x_7 = x_7[1:19]
        # x_8 = x_8[1:19]
        # x_9 = x_9[1:19]

        #print(y_values)
        # print(x_2)
        # print(y_values)

        y_values.pop(1)  # ignore COVID season
        league_pos.pop(1)
        x_2.pop(1)
        x_3.pop(1)
        x_4.pop(1)
        # x_5.pop(1)
        # x_6.pop(1)
        # x_7.pop(1)

        if header == "Infl adjusted arrivals M€":
            x_2.pop(0)
            x_3.pop(-1)
            league_pos.pop(-1)
            y_values.pop(-1)
            x_4.pop(-1)

        # print(len(x_2))
        # print(len(y_values))
        # print("\n")
        # x_4.pop(1)
        # x_8.pop(1)
        # x_9.pop(1)
        #values = file_handling.return_transfermarkt_values_from_csv(team, header)

        # if header == 'Total spectators':
        #     values.pop(0)
        #     league_pos.pop(0) #ignore the latest season for total spectators as the value isn't comparable to other seasons

        #ax.set_xlim(2000, 2022)
        #ax.set_ylim(0, 50000)

        # print(league_pos)
        # print(y_values)
        # print(x_2)
        # print(x_3)
        # print(x_4)
        # print(x_8)
        # print(x_9)
        # print("\n")

        for i in league_pos:
            total_positions.append(i)
        for j in y_values:
            total_values.append(j)
        for k in x_2:
            x_2_total.append(k)
        for k in x_3:
            x_3_total.append(k)
        for k in x_4:
            x_4_total.append(k)
        # for k in x_5:
        #     x_5_total.append(k)
        # for k in x_6:
        #     x_6_total.append(k)
        # for k in x_7:
        #     x_7_total.append(k)
        # for k in x_8:
        #     x_8_total.append(k)
        # for k in x_9:
        #     x_9_total.append(k)
    #slope, intercept = np.polyfit(total_positions, total_values, 1)
    #correlation_calculations = calculations.calculate_pearson_correlation_coefficient(total_positions, total_values)


    # pearson_correlation_coefficient = correlation_calculations[0]
    # covariance = correlation_calculations[1]
    # stdev_x = correlation_calculations[2]
    # stdev_y = correlation_calculations[3]


    # r_calculations = calculations.calculate_r_squared(total_positions, total_values, total_values2)
    #
    # r_squared = r_calculations[0]
    # adjusted_r_squared = r_calculations[1]

    # error_calculations = calculations.calculate_mse_rmse_mae(slope, intercept, total_positions, total_values)
    #
    # mean_squared_error = error_calculations[0]
    # root_mean_squared_error = error_calculations[1]
    # mean_absolute_error = error_calculations[2]

    total_positions_mean = statistics.mean(total_positions)
    total_values_mean = statistics.mean(total_values)
    x_2_mean = statistics.mean(x_2_total)
    x_3_mean = statistics.mean(x_3_total)
    x_4_mean = statistics.mean(x_4_total)
    # x_5_mean = statistics.mean(x_3_total)
    # x_6_mean = statistics.mean(x_4_total)
    # x_7_mean = statistics.mean(x_7_total)
    #x_8_mean = statistics.mean(x_8_total)
    # x_9_mean = statistics.mean(x_9_total)

    x_2_total1 = []
    x_3_total1 = []
    x_4_total1 = []
    x_5_total1 = []
    x_6_total1 = []
    x_7_total1 = []
    x_8_total1 = []
    x_9_total1 = []
    total_positions1 = []
    total_values1 = []


    for i in total_positions:
        total_positions1.append(i - total_positions_mean)
    for i in total_values:
        total_values1.append(i - total_values_mean)
    for i in x_2_total:
        x_2_total1.append(i - x_2_mean)
    for i in x_3_total:
        x_3_total1.append(i - x_3_mean)
    for i in x_4_total:
        x_4_total1.append(i - x_4_mean)
    # for i in x_5_total:
    #     x_5_total1.append(i - x_5_mean)
    # for i in x_6_total:
    #     x_6_total1.append(i - x_6_mean)
    # for i in x_7_total:
    #     x_7_total1.append(i - x_7_mean)
    # for i in x_8_total:
    #     x_8_total1.append(i - x_8_mean)
    # for i in x_9_total:
    #     x_9_total1.append(i - x_9_mean)



        # regression_calculations = calculations.regression_calcs(total_positions, x_2_total, x_3_total, x_4_total,
        #                                                         x_8_total, x_9_total, total_values)

    # with open("esimerkki.txt", "w") as f:
    #     f.write(str(total_positions))
    #     f.write(str(x_2_total1))
    #     f.write(str(x_3_total1))
    #     f.write(str(x_4_total1))
    #     f.write(str(x_8_total))
    #     f.write(str(x_9_total))
    #     f.write(str(total_values))
    #Market values:
    regression_calculations = calculations.regression_calcs(total_positions1, x_2_total1, x_3_total1, x_4_total, total_values)

    #Bought players:
    #regression_calculations = calculations.regression_calcs(total_positions1, x_2_total1, x_3_total, x_4_total, total_values)

    #Attendances:
    #regression_calculations = calculations.regression_calcs(total_positions1, x_2_total1, x_3_total1, x_4_total1, x_5_total, x_6_total, x_7_total, total_values)


    intercept_coefficient = regression_calculations[0][0]
    x_1_coefficient = regression_calculations[0][1]
    x_2_coefficient = regression_calculations[0][2]

    intercept_p_value = regression_calculations[1][0]
    x_1_p_value = regression_calculations[1][1]
    x_2_p_value = regression_calculations[1][2]

    intercept_std_err = regression_calculations[2][0]
    x_1_std_err = regression_calculations[2][1]
    x_2_std_err = regression_calculations[2][2]

    intercept_t_value = regression_calculations[3][0]
    x_1_t_value = regression_calculations[3][1]
    x_2_t_value = regression_calculations[3][2]

    r_squared = regression_calculations[4]
    adjusted_r_squared = regression_calculations[5]



    n = len(total_values)

    # file_handling.calculations_to_csv("regression_results_without_covid_season10.csv", header,
    #                                   ["Total", n, intercept_coefficient, x_1_coefficient, x_2_coefficient,
    #                                    intercept_t_value, x_1_t_value, x_2_t_value,
    #                                    intercept_p_value, x_1_p_value, x_2_p_value,
    #                                    intercept_std_err, x_1_std_err, x_2_std_err,
    #                                    r_squared, adjusted_r_squared])


    # file_handling.calculations_to_csv("regression_results_without_covid_season9.csv", header, ["Total", n, covariance, stdev_x, stdev_y, pearson_correlation_coefficient,
    #                                                                                            r_squared, adjusted_r_squared, mean_squared_error, root_mean_squared_error, mean_absolute_error])

    #plt.plot(total_positions, slope * np.array(total_positions) + intercept, color='red')


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




