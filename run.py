from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from tts import text2, voice2
import os

app = Flask(__name__)
yo = 'wfkhqhofqfcqfcq'
app.config['UPLOAD_FOLDER'] = './static/avatars/'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/show', methods = ['GET','POST'])
def text1():
    text = ""
    print(text)
    if request.method == 'POST':
        # name = request.form['name']
        # print(name)
        file = request.files['img']
        filename = str(file).split("'")
        print(filename[1])
        # filename = request.form['img']
        if file:
            # imagename = secure_filename(image.imagename)
            print(app.config['UPLOAD_FOLDER']+str(filename[1]))
            file.save(os.path.abspath(app.config['UPLOAD_FOLDER']+str(filename[1])))
        print(str(file))
        text = text2(file)
        return render_template('index1.html', text_image = text)

@app.route('/voice',methods = ['GET','POST'])
def voice():
    if request.method == 'POST':
        # name = request.form['name']
        # print(name)
        file = request.files['img']
        voice1 = voice2(file)
        return render_template('voice.html', audios = voice1)

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug = True)