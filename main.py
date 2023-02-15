import file_handling
import img_conversion_and_processing
import extracting_data
import data_visualization
import debt_visualization


def main():
    files_to_convert = file_handling.get_filenames('Financial statements')
    team_and_files = file_handling.get_filenames('Financial statements in csv')
    #global current_team
    #current_team = file_handling.return_cur_team()
    images_dict = img_conversion_and_processing.convert_to_jpg(files_to_convert)
    #img_conversion_and_processing.image_processing(images_dict)
    #extracting_data.main()
    #data = extracting_data.file_reading(team_and_files)
    #data_visualization.scatter_chart(data)
    #debt_visualization.scatter_chart(data)
    #merged_financial_statement = img_conversion_and_processing.merge_images(processed_images)
    #ocr_result_to_txt()


main()