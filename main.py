import pytesseract
from pdf2image import convert_from_path

def main():
    images = convert_from_path('Season 2010-2011 FGR.pdf')

    convert_to_jpg(images)
    image_processing()
    ocr_result(images)


def convert_to_jpg(images):
    images[0].save('testi' + '.jpg', 'JPEG')

def image_processing():
    pass

def ocr_result(images):
    for img in images:
        print(pytesseract.image_to_string(img))


main()