import pytesseract as ts
from PIL import Image
import os

def getDirectory(directory_name):
    vcf_files = [file for file in os.listdir(directory_name)]
    return vcf_files

def main(dictionary_name):
    for i in range(len(getDirectory(dictionary_name))):
        with open('135(1).txt', 'w') as f:
            f.write(ts.image_to_string(Image.open((os.path.join(dictionary_name, getDirectory(dictionary_name)[i])))))
        f.close()


ts.pytesseract.tesseract_cmd = r'C:/Users/jaguar/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
# main('screenshots/')
imgs = ts.image_to_string(Image.open('C:/Users/jaguar/Documents/New Folder (2)/rout front end/rout frontend js/week 9/Screenshot 2023-08-08 022830.png'))
print(imgs)
