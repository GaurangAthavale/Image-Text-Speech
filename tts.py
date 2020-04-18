# import the following libraries 
# will convert the image to text string 
import pytesseract	 
import os
# adds image processing capabilities 
from PIL import Image	 

# converts the text to speech 
# import pyttsx3		 

#translates into the mentioned language 
from googletrans import Translator	 

from gtts import gTTS

# opening an image from the source path 
def text2(image):
    print(image)
    img = Image.open(image)	
    pytesseract.pytesseract.tesseract_cmd = r'C:/Users/HP/AppData/Local/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(img)
    print(text)
    return text

def voice2(image):
    img = Image.open(image)	
    pytesseract.pytesseract.tesseract_cmd = r'C:/Users/HP/AppData/Local/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(img)
    print(text)
    language = 'en'
    output = gTTS(text=text,lang=language, slow=False)
    filename = str(image).split("'")
    print(filename)
    val = filename[1][:filename[1].index(".")]
    name = './static/audio/'+val+".mp3"
    if output:
        output.save(os.path.abspath(name))
    # return os.path.abspath(name)
    return val+".mp3"

    # os.system("start "+name)