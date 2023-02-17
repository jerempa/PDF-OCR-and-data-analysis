from file_operations import file_handling, extracting_data
from data_visualization_and_analysis import *
from optimal_char_recognition import img_conversion_and_processing, img_to_string


def main():
    files_to_convert = file_handling.get_filenames('Financial statements')
    #team_and_files = file_handling.get_filenames('Financial statements in csv')
    #global current_team
    #current_team = file_handling.return_cur_team()
    images_dict = img_conversion_and_processing.convert_to_jpg(files_to_convert)
    #print(images_dict)
   #print(type(image))
    #print(image)
    #images_dict = file_handling.create_img_dicts()
    img_conversion_and_processing.image_processing(images_dict)
    #extracting_data.main()
    # data = extracting_data.file_reading(team_and_files)
    # data_visualization.scatter_chart(data)
    # debt_visualization.scatter_chart(data)
    #fetch_data_from_transfermarkt.get_request()
    #debt_visualization.scatter_chart(data)
    #merged_financial_statement = img_conversion_and_processing.merge_images(processed_images)
    #ocr_result_to_txt()


main()