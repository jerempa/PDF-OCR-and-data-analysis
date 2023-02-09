from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2
import pytesseract
import pandas as pd

import correct_seasons
import img_to_string
import file_handling

def convert_to_jpg(pdf_dict):
    images_dict = dict()
    #i = 0
    for team, f_statements in pdf_dict.items():
        images_list = []
        if team != 'Forest Green Rovers' and team != 'Ipswich Town' and team != 'Blackpool FC':
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
        if team != 'Forest Green Rovers' or team != 'Ipswich town' or team != 'Blackpool FC':
            for img in images:
                processed_images_list = []
                for index, image in enumerate(img):
                    if index <= 5:
                        continue
                    filtering = filter_pages(image)
                    if filtering:
                        image = process_image(image)
                        img_to_string.ocr_result_to_txt(image, team)

                #try:
                #processed_images[team] = np.vstack(processed_images_list)
                starting_season = correct_seasons.return_teams_season(team)
                #merge_images(processed_images, starting_season)
                correct_seasons.get_correct_dates(starting_season, team)
                # except ValueError:
                #     pass
    return processed_images

def filter_pages(image):
    data = pytesseract.image_to_data(image, output_type='data.frame')
    # f = open('testi6.txt', 'a', encoding='utf-8')
    # f.write(pytesseract.image_to_data(image))
    # f.close()
    pala_criteria1 = data['text'].str.lower().str.contains('turnover').any()
    pala_criteria2 = data['text'].str.lower().str.contains('gross').any()
    #pala_criteria3 = data['text'].str.lower().str.contains('interest').any()
    pala_criteria4 = data['text'].str.lower().str.contains('profit').any()

    balance_sheet_criteria1 = data['text'].str.lower().str.contains('debtors').any()
    balance_sheet_criteria2 = data['text'].str.lower().str.contains('share').any()
    balance_sheet_criteria3 = data['text'].str.lower().str.contains('capital').any()

    attachment_criteria1 = data['text'].str.lower().str.contains('wages').any()
    attachment_criteria2 = data['text'].str.lower().str.contains('salaries').any()
    attachment_criteria3 = data['text'].str.lower().str.contains('pension').any()
    attachment_criteria4 = data['text'].str.lower().str.contains('payroll').any()

    #print(pala_criteria4, pala_criteria3, pala_criteria2, pala_criteria1)
    #print(balance_sheet_criteria3, balance_sheet_criteria2, balance_sheet_criteria1)


    if (pala_criteria1 and pala_criteria2 and pala_criteria4) \
            or (balance_sheet_criteria1 and balance_sheet_criteria2 and balance_sheet_criteria3)\
            or ((attachment_criteria1 or attachment_criteria2) and attachment_criteria3 and attachment_criteria4):
        return True
    return False

def process_image(image):
    kernel = np.ones((1, 1), np.uint8)
    image = np.array(image)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    # test_image = cv2.medianBlur(test_image, 3)
    image = cv2.GaussianBlur(image, (3, 3), 0)

    return image

def merge_images(images, season):
    for team in images.keys():
        merged_image = Image.fromarray(images[team])
        correct_seasons.get_correct_dates(season)
        file_handling.create_dir_for_images(merged_image, team, season)
        season = correct_seasons.return_teams_season()
