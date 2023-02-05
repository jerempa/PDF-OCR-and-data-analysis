import pytesseract
from pdf2image import convert_from_path
import numpy as np
import cv2
import os
from PIL import Image

def main():
    #images = convert_from_path('Season 2010-2011 FGR.pdf')
    #test_image = images[7]
    #print(os.getcwd())
    files_to_convert = get_filenames()
    images_dict = convert_to_jpg(files_to_convert)
    processed_images = image_processing(images_dict)
    merged_financial_statement = merge_images(processed_images)
    #ocr_result_to_txt(processed_images)

def get_filenames():
    team_and_files = dict()
    for directory in os.listdir('Financial statements'):
        files = []
        dir = os.path.join('Financial statements', directory)
        if os.path.isdir(dir):
            for filename in os.listdir(dir):
                file = os.path.join(dir, filename)
                if os.path.isfile(file):
                    files.append(filename)
            team_and_files[directory] = files
    return team_and_files #loop through dir that has team sub-dirs, add their files to a dict


def convert_to_jpg(pdf_dict):
    images_dict = dict()
    for team, f_statements in pdf_dict.items():
        images_list = []
        try:
            for file in f_statements:
                path = f'Financial statements/{team}/{file}'
                image = convert_from_path(path)
                images_list.append(image)
                break
        except (IOError, ValueError):
            pass
        images_dict[team] = images_list
    return images_dict #loop through the dict and convert pdfs to jpg, later going to save them also so this doesn't have to be executed every time

def image_processing(images_dict):
    processed_images = {}
    for team, images in images_dict.items():
        processed_images_list = []
        for img in images:
            for image in img:
                kernel = np.ones((1, 1), np.uint8)
                image = np.array(image)
                image = cv2.dilate(image, kernel, iterations=1)
                kernel = np.ones((1, 1), np.uint8)

                image = cv2.erode(image, kernel, iterations=1)
                image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
                # test_image = cv2.medianBlur(test_image, 3)
                image = cv2.GaussianBlur(image, (3, 3), 0)
                processed_images_list.append(image)
        processed_images[team] = np.vstack(processed_images_list)
    return processed_images

def save_processed_images(image, team):
    try:
        os.mkdir(f'{os.getcwd()}\Processed images')
        dirpath = f'{os.getcwd()}\Processed images'
        os.chdir(dirpath)
    except FileExistsError:
        try:
            os.chdir(f'{os.getcwd()}\Processed images')
            os.mkdir(f'{os.getcwd()}\{team}')
            os.chdir(f'{os.getcwd()}\{team}')
            image.save(f'{team} financial statements.jpg', 'JPEG')
        except FileExistsError:
            pass


def merge_images(images):
    # img = Image.open('example.jpg')
    # width, height = img.size
    for team in images.keys():
        merged_image = Image.fromarray(images[team])
        save_processed_images(merged_image, team)

def ocr_result_to_txt(images):
    f = open("Financial statements in txt/Forest Green Rovers/Season1011.txt", "a", encoding="utf-8")
    for img in images:
        f.write(pytesseract.image_to_string(img))
    f.close()


main()