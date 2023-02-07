import pytesseract
from pdf2image import convert_from_path
import numpy as np
import cv2
import os
from PIL import Image
from datetime import datetime, timedelta

starting_seasons = {'Forest Green Rovers': '2010-2011'}

def main():
    #images = convert_from_path('Season 2010-2011 FGR.pdf')
    #test_image = images[7]
    #print(os.getcwd())
    files_to_convert = get_filenames()
    images_dict = convert_to_jpg(files_to_convert)
    processed_images = image_processing(images_dict)
    #merged_financial_statement = merge_images(processed_images)
    #ocr_result_to_txt()

def get_filenames():
    team_and_files = dict()
    for directory in os.listdir('Financial statements'):
        files = []
        dir = os.path.join('Financial statements', directory)
        if os.path.isdir(dir):
            global current_team
            current_team = directory
            for filename in os.listdir(dir):
                file = os.path.join(dir, filename)
                if os.path.isfile(file):
                    files.append(filename)
            team_and_files[directory] = files
    return team_and_files #loop through dir that has team sub-dirs, add their files to a dict


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
    return images_dict #loop through the dict and convert pdfs to jpg, later going to save them also so this doesn't have to be executed every time

def image_processing(images_dict):
    processed_images = {}
    for team, images in images_dict.items():
        for img in images:
            #print(images, len(images))
            processed_images_list = []
            for index, image in enumerate(img):
                # if index <= 5:
                #     continue
                kernel = np.ones((1, 1), np.uint8)
                image = np.array(image)
                image = cv2.dilate(image, kernel, iterations=1)
                kernel = np.ones((1, 1), np.uint8)
                image = cv2.erode(image, kernel, iterations=1)
                image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
                # test_image = cv2.medianBlur(test_image, 3)
                image = cv2.GaussianBlur(image, (3, 3), 0)
                processed_images_list.append(image)
                ocr_result_to_txt(image)
            processed_images[team] = np.vstack(processed_images_list)
            #break
            get_correct_dates(starting_seasons[current_team])
            #print(len(processed_images_list))
            #merge_images(processed_images)
    return processed_images

def create_dir_for_images(image, team, f_statement_season):
    try:
        os.mkdir(f'{os.getcwd()}\Processed images')
        os.chdir(f'{os.getcwd()}\Processed images')
        save_files(image, team, f_statement_season)
        os.chdir('..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\Processed images')
        save_files(image, team, f_statement_season)
        os.chdir('..')

def save_files(image, team, f_statement_season):
    #f_statement_season = starting_seasons[team]
    try:
        os.mkdir(f'{os.getcwd()}\{team}')
        os.chdir(f'{os.getcwd()}\{team}')
        image.save(f'{team} financial statement {f_statement_season}.jpg', 'JPEG')
        os.chdir('..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\{team}')
        image.save(f'{team} financial statement {f_statement_season}.jpg', 'JPEG')
        os.chdir('..')
    #get_correct_dates(team, f_statement_season)

def get_correct_dates(date_str):
    start_year, end_year = [int(x) for x in date_str.split("-")]
    #start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)

    new_start_date = end_date
    new_end_date = end_date + timedelta(days=365)

    new_date_str = new_start_date.strftime("%Y") + "-" + new_end_date.strftime("%Y")
    starting_seasons[current_team] = new_date_str



def merge_images(images):
    for team in images.keys():
        merged_image = Image.fromarray(images[team])
        f_statement_season = starting_seasons[team]
        #print(merged_image)
        create_dir_for_images(merged_image, team, f_statement_season)

def ocr_result_to_txt(img):
    #print(os.getcwd(), current_team)
    #print(starting_seasons[current_team], os.getcwd())
    #print(os.path.basename(os.getcwd()))
    # if os.path.basename(os.getcwd()) == 'Financial statements in txt':
    #     try:
    #         os.mkdir(f'{os.getcwd()}/{current_team}')
    #         os.chdir(f'{os.getcwd()}/{current_team}')
    #     except FileExistsError:
    #         pass
    #print(os.getcwd())
    if os.path.basename(os.getcwd()) == current_team:
        f = open(f'{current_team} {starting_seasons[current_team]}.txt', 'a', encoding='utf-8')
        f.write(pytesseract.image_to_string(img))
        f.close()
    create_dir_for_txt()
    #os.chdir(f'{os.getcwd()}\Financial Statements in txt')

# def ocr_result_to_txt(img):
#     pass


# def ocr_result_to_txt(img):
#     dir_path = f'{os.getcwd()}\Processed images'
#     os.chdir(dir_path)
#     f = None
#     for team in os.listdir(dir_path):
#         dir_path = os.path.join(dir_path, team)
#         os.chdir(dir_path)
#         for filename in os.listdir(dir_path):
#             print(os.getcwd())
#             season = filename[len(filename) - 13: len(filename) - 4]
#             image = Image.open(filename)
#             image_text = pytesseract.image_to_string(image)
#             #print(os.getcwd())
#             create_dir_for_txt(team, season)
#             #print(image_text)
#             #f = open(f"\{team}\{season}.txt", "w", encoding="utf-8")
#             #f.write(image.text)
#             os.chdir(dir_path)
#     #f.close()

    #f = open("Financial statements in txt/Forest Green Rovers/Season1011.txt", "a", encoding="utf-8")
    # for img in images:
    #     f.write(pytesseract.image_to_string(img))
    #f.close()

def create_dir_for_txt():
    #print(os.path.basename(os.getcwd()), os.getcwd())
    #print(starting_seasons[current_team], os.getcwd())
    try:
        if os.path.basename(os.getcwd()) == current_team:
            pass
        elif os.path.basename(os.getcwd()) == 'Financial statements in txt':
            try:
                os.mkdir(f'{os.getcwd()}/{current_team}')
                os.chdir(f'{os.getcwd()}/{current_team}')
            except FileExistsError:
                os.chdir(f'{os.getcwd()}/{current_team}')
        else:
            os.mkdir(f'{os.getcwd()}/Financial statements in txt')
            os.chdir(f'{os.getcwd()}/Financial statements in txt')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}/Financial statements in txt') #changing and making directories, depending on where the user is


main()