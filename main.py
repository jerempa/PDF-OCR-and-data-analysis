from file_operations import file_handling, extracting_data
from data_visualization_and_analysis import data_visualization, debt_visualization,\
    values_for_analysis, calculations, financial_statement_data_visualization, transfermarkt_data_visualization, time_series_analysis
from data_fetchers import fetch_data_from_transfermarkt, df_operations, download_pdfs, fetch_data_from_worldfootball, fetch_season_data_from_wiki
from optimal_char_recognition import img_conversion_and_processing, img_to_string

import json
import ast
import csv
import pandas as pd


def main():
    #team_and_files = file_handling.get_filenames('Financial statements in csv')

    # files_to_convert = file_handling.get_filenames('Financial statements')
    # images_dict = img_conversion_and_processing.convert_to_jpg(files_to_convert)
    # img_conversion_and_processing.image_processing(images_dict) #writing pdf info to csv

    #images_dict = file_handling.create_img_dicts()

    #download_pdfs.download_financial_statements() #download pdfs from web

    #extracting_data.main() #extract financial statement data from csv


    #file_handling.read_financial_statement_values()
    # data = extracting_data.file_reading(team_and_files)
    # data_visualization.scatter_chart(data)
    # debt_visualization.scatter_chart(data)

    #values = fetch_data_from_transfermarkt.main() #fetch data from transfermarkt

    #df_operations.print_df() #print the transfermarkt dataframes

    #financial_statement_data_visualization.scatter_chart()


    #transfermarkt_data_visualization.line_plot_and_color_visualization()

    #time_series_analysis.time_series()

   transfermarkt_data_visualization.scatter_chart()
        # city_list = ['Bournemouth, Christchurch and Poole', "Blackburn with Darwen", "Blackpool", "Greenwich", "Bolton", "Hammersmith and Fulham", 'Hounslow', "Brighton and Hove", "Cardiff", "Derby", "Kirklees", "Kingston upon Hull, City of",
    #              "Ipswich", "Leeds", "Leicester", "Norwich", "Nottingham", "Portsmouth", "Reading", "Sheffield", "Southampton", "Stoke-on-Trent", "Sunderland", "Swansea", "Wigan", "Wolverhampton"
    #              ]
    # new_dict = None
    # with open("scraped_data9.txt", 'r') as f:
    #     data = f.read()
    #     data = json.loads(data)
    #     # print(type(data), data)
    #     new_dict = data
    #     # print(json.dumps(data))
    #     # data = data.replace("'", '"')
    #     # data = data.replace(None, 'null')
    #     # print(data)
    #
    # new_values = []
    # for i in new_dict:
    #     for item, value in i.items():
    #         for key, value1 in value.items():
    #             print(item, key, len(value1), value1)

    #kingston upon hull viimeisin mikä tehty

    #df = pd.read_csv('MYEB1_detailed_population_estimates_series_UK_(2020_geog21).csv')

    #filtered_df = df[df['laname21'].isin(city_list)]

    #yearly_population = filtered_df.groupby('laname21').sum().iloc[:, 4:]

    # Convert the result to a dictionary
    #result = yearly_population.to_dict('list')

    # Print the result
    #print(result)

    # city_populations = []
    #
    # for city in city_list:
    #     # Get the population data for the city
    #     city_data = df.loc[df['laname21'] == city]
    #
    #     # Create a dictionary of the city and its population data
    #     city_dict = {
    #         city: {
    #             '2001': city_data['population_2001'].sum(),
    #             '2002': city_data['population_2002'].sum(),
    #             '2003': city_data['population_2003'].sum(),
    #             '2004': city_data['population_2004'].sum(),
    #             '2005': city_data['population_2005'].sum(),
    #             '2006': city_data['population_2006'].sum(),
    #             '2007': city_data['population_2007'].sum(),
    #             '2008': city_data['population_2008'].sum(),
    #             '2009': city_data['population_2009'].sum(),
    #             '2010': city_data['population_2010'].sum(),
    #             '2011': city_data['population_2011'].sum(),
    #             '2012': city_data['population_2012'].sum(),
    #             '2013': city_data['population_2013'].sum(),
    #             '2014': city_data['population_2014'].sum(),
    #             '2015': city_data['population_2015'].sum(),
    #             '2016': city_data['population_2016'].sum(),
    #             '2017': city_data['population_2017'].sum(),
    #             '2018': city_data['population_2018'].sum(),
    #             '2019': city_data['population_2019'].sum(),
    #             '2020': city_data['population_2020'].sum()
    #         }
    #     }
    #
    #     # Add the city dictionary to the list of city populations
    #     city_populations.append(city_dict)
    #
    # # Print the list of city populations
    # print(city_populations)
    #fetch_data_from_worldfootball.main()
    # capa_dict = {}
    #
    # with open("stadium_cap2.txt", 'r') as f:
    #     data = f.read()
    #     #data = json.loads(data)
    #     data = ast.literal_eval(data)
    #     #print(data)
    #     #print(type(ast.literal_eval(data)))
    #     for team, values in data.items():
    #         #print(team, values)
    #         capacity_list = []
    #         for year, capa in values.items():
    #             capacity_list.append(capa)
    #         capa_dict[team] = capacity_list
    # # #print(json.dumps(capa_dict))
    # #
    # # #capa_dict = json.dumps(capa_dict)
    # #
    # #print(capa_dict)
    #     capa_dict = {
    #     'AFC Bournemouth': [172] * 24,
    #     'Blackburn Rovers': [45] * 24,
    #     'Blackpool FC': [85] * 24,
    #     'Bolton Wanderers': [25] * 24,
    #     'Brentford FC': [0] * 24,
    #     'Brighton & Hove Albion': [125] * 24,
    #     'Cardiff City': [0] * 24,
    #     'Charlton Athletic': [0] * 24,
    #     'Derby County': [65] * 24,
    #     'Huddersfield Town': [30] * 24,
    #     'Hull City': [100] * 24,
    #     'Ipswich Town': [130] * 24,
    #     'Leeds United': [0] * 24,
    #     'Leicester City': [70] * 24,
    #     'Norwich City': [250] * 24,
    #     'Nottingham Forest': [70] * 24,
    #     'Portsmouth FC': [120] * 24,
    #     'Queens Park Rangers': [0] * 24,
    #     'Reading FC': [70] * 24,
    #     'Sheffield United': [0] * 24,
    #     'Southampton FC': [130] * 24,
    #     'Stoke City': [65] * 24,
    #     'Sunderland AFC': [20] * 24,
    #     'Swansea City': [75] * 24,
    #     'Wigan Athletic': [35] * 24,
    #     'Wolverhampton Wanderers': [30] * 24
    # }
    #     lst = []
    #     # # #
    #     with open("scraped_data9.txt", "r") as file:
    #         data = file.read()
    #         data = json.loads(data)
    #         #print(data)
    #
    #         for i in data:
    #             for team, values in i.items():
    #                 #print(team, values)
    #                 one_list = [1] * 24
    #                 zero_list = [0] * 24
    #                 #for avain, arvo in capa_dict.items():
    #                     #print(team, avain, arvo)
    #                 if team in ['Bolton Wanderers', 'Brentford FC', 'Charlton Athletic', 'Huddersfield Town', 'Leeds United', 'Queens Park Rangers', 'Sheffield United', 'Sunderland AFC', 'Wigan Athletic', 'Wolverhampton Wanderers']:
    #                     #arvo.reverse()
    #                     #print(avain, arvo, team)
    #                     i[team]['Only football team in top 4 leagues in the metropolitan county'] = zero_list
    #                 else:
    #                     i[team]['Only football team in top 4 leagues in the metropolitan county'] = one_list
    #
    #                 #print(avain, arvo, team)
    #             #print(json.dumps(i))
    #             lst.append(json.dumps(i))
    #
    #     print(lst)
                # for key, value in values.items():
                #     print(team, key, value)


    #
    #     new_dict = data

    #print(json.loads(new_dict))
    #fetch_season_data_from_wiki.main()

    #calculations.main() #calculations of of dataframes

    #calculations.show_average_attendace_to_capacity() #calculations of of dataframes

    #file_handling.write_scraped_data_to_file(values) #write df data to file to avoid unnecessary requests

    #merged_financial_statement = img_conversion_and_processing.merge_images(processed_images) #merge images to one file



main()