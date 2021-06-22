try:
    from PIL import Image, ImageGrab
    from pynput.keyboard import Key, Controller
except ImportError:
    import Image
import pytesseract, pynput, time

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text_to_search_for = "Item Drop Rate"
    keyboard = Controller()

    while(True):
        cubed_lines = []
        count = 0
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(.5)
        #line 1
        im = ImageGrab.grab(bbox=(850,500,1170,520))
        im.save('maple_tab1.png','PNG')
        cubed_lines.append(pytesseract.image_to_string(Image.open('maple_tab1.png')))
        #line 2
        im = ImageGrab.grab(bbox=(850,524,1100,538))
        im.save('maple_tab2.png','PNG')
        cubed_lines.append(pytesseract.image_to_string(Image.open('maple_tab2.png')))
        #line 3
        im = ImageGrab.grab(bbox=(850,540,1100,557))
        im.save('maple_tab3.png','PNG')
        cubed_lines.append(pytesseract.image_to_string(Image.open('maple_tab3.png')))
        
        for string in cubed_lines:
            print(string)
            if (string.find(text_to_search_for) != -1):
                count += 1 
            # if ((string.find(text_to_search_for) != -1 or string.find("All") != -1) and string.find("%") != -1):
            #     count += 1 

        if count == 3:
            quit()
        print(count)
if __name__ == "__main__":
    main()