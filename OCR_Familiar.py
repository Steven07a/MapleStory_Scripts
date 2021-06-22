try:
    from PIL import Image, ImageGrab
    from pynput.mouse import Button, Controller as MouseController
    from pynput.keyboard import Key, Controller as KeyboardController
except ImportError:
    import Image
import pytesseract, pynput, time

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text_to_search_for = "Attacks ignore"
    mouse = MouseController()
    keyboard = KeyboardController()
    while(True):
        cubed_lines = []
        count = 0
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        #line 1
        im = ImageGrab.grab(bbox=(615,680,900,699))
        im.save('maple_tab1.png','PNG')
        cubed_lines.append(pytesseract.image_to_string(Image.open('maple_tab1.png')))
        #line 2
        im = ImageGrab.grab(bbox=(615,699,900,712))
        im.save('maple_tab2.png','PNG')
        cubed_lines.append(pytesseract.image_to_string(Image.open('maple_tab2.png')))
        
      
        for string in cubed_lines:
            print(string)
            if (string.find(text_to_search_for) != -1):
                count += 1 
            print(count)
        if count == 2:
            quit()
if __name__ == "__main__":
    main()