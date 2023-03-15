from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2
import pytesseract

import correct_seasons
from optimal_char_recognition import img_to_string
from file_operations import file_handling


def convert_to_jpg(pdf_dict):
    #print(pdf_dict)
    images_dict = dict()
    #i = 0
    #print("testi")
    for team, f_statements in pdf_dict.items():
        images_list = []
        try:
            for file in f_statements:
                path = f'Financial statements/{team}/{file}'
                image = convert_from_path(path)
                images_list.append(image)
                #season = file[7:len(file) - 5 - len(team)]
                #file_handling.create_dir_for_images(image, team, season)
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
        for img in images:
            processed_images_list = []
            for index, image in enumerate(img):
                # if index <= 6:
                #    continue
                #filtering = filter_pages(image)
                #if filtering:
                image = process_image(image)
                data_for_formatting = formatting_data(image)
                img_to_string.ocr_result_to_csv(data_for_formatting, team)
                    #img_to_string.ocr_result_to_txt(image, team)
                #break

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

    pala_criteria1 = None
    pala_criteria3 = None
    pala_criteria4 = None
    pala_criteria6 = None

    balance_sheet_criteria1 = None
    balance_sheet_criteria2 = None
    balance_sheet_criteria3 = None

    attachment_criteria1 = None
    attachment_criteria2 = None
    attachment_criteria3 = None
    attachment_criteria4 = None
    try:
        pala_criteria1 = data['text'].str.lower().str.contains('turnover').any()
        # #pala_criteria2 = data['text'].str.lower().str.contains('gross').any()
        pala_criteria3 = data['text'].str.lower().str.contains('revenue').any()
        pala_criteria4 = data['text'].str.lower().str.contains('profit').any()
        pala_criteria6 = data['text'].str.lower().str.contains('loss').any()
        pala_criteria5 = data['text'].str.lower().str.contains('interest').any()

        balance_sheet_criteria1 = data['text'].str.lower().str.contains('stocks').any()
        balance_sheet_criteria3 = data['text'].str.lower().str.contains('stock').any()
        #balance_sheet_criteria2 = data['text'].str.lower().str.contains('assets').any()
        # balance_sheet_criteria2 = data['text'].str.lower().str.contains('share').any()
        balance_sheet_criteria2 = data['text'].str.lower().str.contains('debtors').any()

        attachment_criteria1 = data['text'].str.lower().str.contains('wages').any()
        attachment_criteria2 = data['text'].str.lower().str.contains('salaries').any()
        attachment_criteria3 = data['text'].str.lower().str.contains('pension').any()
        attachment_criteria4 = data['text'].str.lower().str.contains('staff').any()
    except AttributeError:
        pass
    # pound_sign = data['text'].str.lower().str.contains('£').any()
    # note = data['text'].str.lower().str.contains('note').any()
    # profit = data['text'].str.lower().str.contains('profit').any()

    #print(pala_criteria4, pala_criteria3, pala_criteria2, pala_criteria1)
    #print(balance_sheet_criteria3, balance_sheet_criteria2, balance_sheet_criteria1)


    if ((pala_criteria4 or pala_criteria6) and (pala_criteria1 or pala_criteria3)) \
            or ((balance_sheet_criteria1 or balance_sheet_criteria3) and balance_sheet_criteria2)\
            or ((attachment_criteria1 or attachment_criteria2) and (attachment_criteria3 or attachment_criteria4)):
        return True
    return False

def formatting_data(image):
    data = pytesseract.image_to_data(image, output_type='data.frame')

    texts = data["text"]
    lefts = data["left"]
    tops = data["top"]

    sorted_data = sorted(zip(texts, lefts, tops), key=lambda x: (x[2], x[1]))

    return sorted_data

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
        file_handling.create_dir_for_processed_images(merged_image, team, season)
        season = correct_seasons.return_teams_season()
