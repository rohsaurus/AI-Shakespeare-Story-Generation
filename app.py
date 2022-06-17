from flask import Flask, request, render_template, jsonify
from templates import *


app = Flask(__name__)

def inputStory(text1): 
    #send text1 to the method that will run the ai model
    #return the output of the model

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
