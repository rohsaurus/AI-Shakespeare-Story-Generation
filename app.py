from flask import Flask, request, render_template, jsonify
from templates import *
from run import *
from deepai import *

app = Flask(__name__)

def inputStory(text1): 
   #return run(text1) 
   return deepAi(text1)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET', 'POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    # text2 = request.form['text2']
    combine = inputStory(text1)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=False)
