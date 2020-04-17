# import the following libraries 
# will convert the image to text string 
import pytesseract	 
import os
# adds image processing capabilities 
from PIL import Image	 

# converts the text to speech 
import pyttsx3		 

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

# text2('./test1.png')


# language = 'en'

# output = gTTS(text=text,lang=language, slow=False)

# output.save("hand.mp3")

# os.system("start hand.mp3")