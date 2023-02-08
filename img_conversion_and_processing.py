from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2

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

# def image_processing(images_dict):
#     processed_images = {}
#     for team, images in images_dict.items():
#         for img in images:
#             #print(images, len(images))
#             processed_images_list = []
#             for index, image in enumerate(img):
#                 # if index <= 5:
#                 #     continue
#                 kernel = np.ones((1, 1), np.uint8)
#                 image = np.array(image)
#                 image = cv2.dilate(image, kernel, iterations=1)
#                 kernel = np.ones((1, 1), np.uint8)
#                 image = cv2.erode(image, kernel, iterations=1)
#                 image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#                 # test_image = cv2.medianBlur(test_image, 3)
#                 image = cv2.GaussianBlur(image, (3, 3), 0)
#                 processed_images_list.append(image)
#                 ocr_result_to_txt(image)
#             processed_images[team] = np.vstack(processed_images_list)
#             #break
#             get_correct_dates(starting_seasons[current_team])
#             #print(len(processed_images_list))
#             #merge_images(processed_images)
#     return processed_images