import pytesseract
from pdf2image import convert_from_path
import numpy as np
import cv2

def main():
    images = convert_from_path('Season 2010-2011 FGR.pdf')
    test_image = images[7]
    #convert_to_jpg(images)
    processed_images = image_processing(images)
    ocr_result_to_txt(processed_images)


def convert_to_jpg(images):
    images[7].save('testi1.jpg', 'JPEG')

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
    f = open("Forest Green Rovers/Season1011.txt", "a", encoding="utf-8")
    for img in images:
        f.write(pytesseract.image_to_string(img))
    f.close()


main()