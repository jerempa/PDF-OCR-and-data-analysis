import pytesseract
from pdf2image import convert_from_path
import numpy as np
import cv2
import os

def main():
    #images = convert_from_path('Season 2010-2011 FGR.pdf')
    test_image = images[7]
    files_to_convert = get_filenames()
    convert_to_jpg(files_to_convert)
    #processed_images = image_processing(images)
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


def convert_to_jpg(dict):
    #for key, value in dict.items():

def image_processing(images):
    processed_images = []
    for img in images:
        kernel = np.ones((1, 1), np.uint8)
        image = np.array(img)
        image = cv2.dilate(image, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)

        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        # test_image = cv2.medianBlur(test_image, 3)
        image = cv2.GaussianBlur(image, (3, 3), 0)
        processed_images.append(image)
    return processed_images


def ocr_result_to_txt(images):
    f = open("Financial statements in txt/Forest Green Rovers/Season1011.txt", "a", encoding="utf-8")
    for img in images:
        f.write(pytesseract.image_to_string(img))
    f.close()


main()