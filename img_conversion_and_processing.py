from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2

import correct_seasons
import img_to_string
import file_handling

def convert_to_jpg(pdf_dict):
    images_dict = dict()
    #i = 0
    for team, f_statements in pdf_dict.items():
        images_list = []
        try:
            for file in f_statements:
                path = f'Financial statements/{team}/{file}'
                image = convert_from_path(path)
                images_list.append(image)
                #print(file)
                #break
                # i += 1
                # if i == 2:
                #     break
        except (IOError, ValueError):
            pass
        images_dict[team] = images_list
    return images_dict #loop through the dict and convert pdfs to jpg

def image_processing(images_dict):
    processed_images = {}
    for team, images in images_dict.items():
        if team != 'Forest Green Rovers':
            for img in images:
                processed_images_list = []
                for index, image in enumerate(img):
                    kernel = np.ones((1, 1), np.uint8)
                    image = np.array(image)
                    image = cv2.dilate(image, kernel, iterations=1)
                    kernel = np.ones((1, 1), np.uint8)
                    image = cv2.erode(image, kernel, iterations=1)
                    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
                    # test_image = cv2.medianBlur(test_image, 3)
                    image = cv2.GaussianBlur(image, (3, 3), 0)
                    processed_images_list.append(image)
                    img_to_string.ocr_result_to_txt(image)
                processed_images[team] = np.vstack(processed_images_list)
                starting_season = correct_seasons.return_teams_starting_season()
                correct_seasons.get_correct_dates(starting_season)
    return processed_images

def merge_images(images):
    for team in images.keys():
        merged_image = Image.fromarray(images[team])
        f_statement_season = correct_seasons.return_first_season()
        #print(merged_image)
        file_handling.create_dir_for_images(merged_image, team, f_statement_season)