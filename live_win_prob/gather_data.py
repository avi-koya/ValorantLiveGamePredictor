import pyautogui as py

def gather_data():
    box = (360, 40, 375, 375)
    py.screenshot("map.png", region=box)

def main():
    gather_data()