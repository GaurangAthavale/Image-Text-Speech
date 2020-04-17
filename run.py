from flask import Flask, render_template, request
from tts import text2

app = Flask(__name__)
yo = 'wfkhqhofqfcqfcq'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/show', methods = ['GET','POST'])
def text1():
    text = ""
    print(text)
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        image = request.form['img']
        print(str(image))
        text = text2(image)
        return render_template('index1.html', text_image = text)

if __name__ == '__main__':
    app.run(debug = True)