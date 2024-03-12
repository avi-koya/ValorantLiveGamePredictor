import pyautogui as py
import pytesseract as pt

def gather_data():
    pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    box = (360, 40, 375, 375)
    py.screenshot("map.png", region=box)
    box = (1245, 22, 70, 50)
    py.screenshot("time.png", region=box)
    time_stamp = pt.image_to_string('time.png')
           # 'time.png', lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789,: -c page_separator=''')
def main():
    gather_data()