# import the following libraries 
# will convert the image to text string 
import pytesseract	 
import os
from werkzeug.utils import secure_filename
# adds image processing capabilities 
from PIL import Image	 
import urllib3
# converts the text to speech 
# import pyttsx3		 

#translates into the mentioned language 
from googletrans import Translator	 

from gtts import gTTS


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# opening an image from the source path 
def text2(image):
    print(image)
    img = Image.open(image)	
    pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'
    text = pytesseract.image_to_string(img)
    # print(text.split("\n"))
    text = text.split("\n")
    return text

def voice2(image):
    img = Image.open(image)	
    pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'
    text = pytesseract.image_to_string(img)
    print(text)
    language = 'en'
    output = gTTS(text=text,lang=language, slow=False)
    filename = str(image).split("'")
    print(filename)
    # z = filename[1].secure_filename(image.z)
    path = './static/avatars/'+str(filename[1])
    image.save(os.path.abspath(path))
    val = filename[1][:filename[1].index(".")]
    name = './static/audio/'+val+".mp3"
    if output:
        output.save(os.path.abspath(name))
    # return os.path.abspath(name)
    return val+".mp3",filename[1]

    # os.system("start "+name)