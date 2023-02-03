import pytesseract
from pdf2image import convert_from_path

def main():
    images = convert_from_path('Season 2010-2011 FGR.pdf')

    convert_to_jpg(images)
    image_processing()
    ocr_result_to_txt(images)


def convert_to_jpg(images):
    images[0].save('testi' + '.jpg', 'JPEG')

def image_processing():
    pass

def ocr_result_to_txt(images):
    f = open("Forest Green Rovers/Season1011.txt", "a", encoding="utf-8")
    for img in images:
        f.write(pytesseract.image_to_string(img))
    f.close()


main()