from file_operations import file_handling, extracting_data
from data_visualization_and_analysis import data_visualization, debt_visualization, values_for_analysis, league_level_charts, calculations
from data_fetchers import fetch_data_from_transfermarkt, df_operations
from optimal_char_recognition import img_conversion_and_processing, img_to_string


def main():
    #files_to_convert = file_handling.get_filenames('Financial statements')
    #team_and_files = file_handling.get_filenames('Financial statements in csv')
    #global current_team
    #current_team = file_handling.return_cur_team()
    #images_dict = img_conversion_and_processing.convert_to_jpg(files_to_convert)
    #print(images_dict)
   #print(type(image))
    #print(image)
    #images_dict = file_handling.create_img_dicts()
    #img_conversion_and_processing.image_processing(images_dict)
    #extracting_data.main()
    # data = extracting_data.file_reading(team_and_files)
    # data_visualization.scatter_chart(data)
    # debt_visualization.scatter_chart(data)
    #values = fetch_data_from_transfermarkt.get_request()
    #print(values)
    #df_operations.print_df()
    #league_level_charts.line_plot()
    calculations.main()
    #calculations.show_average_attendace_to_capacity()
    #values_for_analysis.league_tier_throughout_years()
    #df_operations.return_attendance_percentage('Brighton & Hove Albion', None)
    #ori = file_handling.return_scraped_data_dict()
    #file_handling.reverse_lists(ori)
    #file_handling.write_scraped_data_to_file(values)
    #debt_visualization.scatter_chart(data)
    #merged_financial_statement = img_conversion_and_processing.merge_images(processed_images)
    #ocr_result_to_txt()


main()