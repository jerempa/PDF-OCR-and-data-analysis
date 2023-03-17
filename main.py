from file_operations import file_handling, extracting_data
from data_visualization_and_analysis import data_visualization, debt_visualization,\
    values_for_analysis, calculations, financial_statement_data_visualization, transfermarkt_data_visualization, time_series_analysis
from data_fetchers import fetch_data_from_transfermarkt, df_operations, download_pdfs, fetch_data_from_worldfootball, fetch_season_data_from_wiki
from optimal_char_recognition import img_conversion_and_processing, img_to_string

import json
import ast


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

    #fetch_data_from_worldfootball.main()
    # capa_dict = {}
    #
    # with open("stadium_capacities1.txt", 'r') as f:
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
    #print(json.dumps(capa_dict))

    #capa_dict = json.dumps(capa_dict)

    #print(capa_dict)
    # lst = []
    #
    # with open("scraped_data7.txt", "r") as file:
    #     data = file.read()
    #     data = json.loads(data)
    #     #print(data)
    #
    #     for i in data:
    #         for team, values in i.items():
    #             #print(team, values)
    #             for avain, arvo in capa_dict.items():
    #                 if avain == team:
    #                     i[team]['Stadium capacity'] = arvo
    #                     #print(avain, arvo, team)
    #         #print(json.dumps(i))
    #         lst.append(json.dumps(i))
    #
    # print(lst)
                # for key, value in values.items():
                #     print(team, key, value)


    # new_dict = None
    # with open("financial statement data.txt", 'r') as f:
    #     data = f.read()
    #     data = json.loads(data)
    #     print(type(data), data)
    #     new_dict = data
    #     #print(json.dumps(data))
    #     #data = data.replace("'", '"')
    #     #data = data.replace(None, 'null')
    #     #print(data)
    #
    # new_values = []
    # for i in new_dict:
    #     for item, value in i.items():
    #         for key, value1 in value.items():
    #             print(item,key,  len(value1), value1)
    #
    #     new_dict = data

    #print(json.loads(new_dict))
    #fetch_season_data_from_wiki.main()

    #calculations.main() #calculations of of dataframes

    #calculations.show_average_attendace_to_capacity() #calculations of of dataframes

    #file_handling.write_scraped_data_to_file(values) #write df data to file to avoid unnecessary requests

    #merged_financial_statement = img_conversion_and_processing.merge_images(processed_images) #merge images to one file



main()