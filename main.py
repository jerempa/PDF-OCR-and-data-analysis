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

    #swansea, brighton palkat
    #revenue bolton


    #file_handling.read_financial_statement_values()
    # data = extracting_data.file_reading(team_and_files)
    # data_visualization.scatter_chart(data)
    # debt_visualization.scatter_chart(data)

    #values = fetch_data_from_transfermarkt.main() #fetch data from transfermarkt

    #df_operations.print_df() #print the transfermarkt dataframes
    #transfermarkt_data_visualization.scatter_chart()

    financial_statement_data_visualization.scatter_chart()


    #transfermarkt_data_visualization.line_plot_and_color_visualization()

    #time_series_analysis.time_series()

    #fetch_season_data_from_wiki.main()

    #calculations.main() #calculations of of dataframes

    #calculations.show_average_attendace_to_capacity() #calculations of of dataframes

    #file_handling.write_scraped_data_to_file(values) #write df data to file to avoid unnecessary requests

    #merged_financial_statement = img_conversion_and_processing.merge_images(processed_images) #merge images to one file



main()