import file_handling
import img_conversion_and_processing
import extracting_data

#starting_seasons = {'Forest Green Rovers': '2010-2011', 'Ipswich Town': '1999-2000'}

def main():
    files_to_convert = file_handling.get_filenames('Financial statements')
    #global current_team
    #current_team = file_handling.return_cur_team()
    images_dict = img_conversion_and_processing.convert_to_jpg(files_to_convert)
    img_conversion_and_processing.image_processing(images_dict)
    #extracting_data.reg_exp_extraction()
    #merged_financial_statement = img_conversion_and_processing.merge_images(processed_images)
    #ocr_result_to_txt()


main()