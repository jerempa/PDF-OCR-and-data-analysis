from file_operations import file_handling, extracting_data
from data_visualization_and_analysis import data_visualization, debt_visualization,\
    values_for_analysis, league_level_charts, calculations, add_missing_rows_to_df
from data_fetchers import fetch_data_from_transfermarkt, df_operations, download_pdfs, fetch_data_from_worldfootball
from optimal_char_recognition import img_conversion_and_processing, img_to_string

import json


def main():
    #team_and_files = file_handling.get_filenames('Financial statements in csv')

    # files_to_convert = file_handling.get_filenames('Financial statements')
    # images_dict = img_conversion_and_processing.convert_to_jpg(files_to_convert)
    # img_conversion_and_processing.image_processing(images_dict) #writing pdf info to csv

    #images_dict = file_handling.create_img_dicts()

    #download_pdfs.download_financial_statements() #download pdfs from web

    #extracting_data.main() #extract financial statement data from csv

    # data = extracting_data.file_reading(team_and_files)
    # data_visualization.scatter_chart(data)
    # debt_visualization.scatter_chart(data)

    #values = fetch_data_from_transfermarkt.get_request() #fetch data from transfermarkt

    #df_operations.print_df() #print the transfermarkt dataframes

    #file_handling.return_scraped_data_dict_attendances()

    #league_level_charts.line_plot() #plotting transfermarkt data

    #fetch_data_from_worldfootball.get_request()

    #df_operations.return_attendance_percentage(None, None)


    #calculations.main() #calculations of of dataframes

    #add_missing_rows_to_df.main() #add manually missing rows to df (not ready yet)

    #calculations.show_average_attendace_to_capacity() #calculations of of dataframes

    #values_for_analysis.league_tier_throughout_years() #cleanse the dataframe values

    #df_operations.return_attendance_percentage('Brighton & Hove Albion', None)

    #file_handling.write_scraped_data_to_file(values) #write df data to file to avoid unnecessary requests

    #debt_visualization.scatter_chart(data) #data visualization (not ready)

    #merged_financial_statement = img_conversion_and_processing.merge_images(processed_images) #merge images to one file



main()