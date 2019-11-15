from flask import Flask, request
from caesar import rotate_character


app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin 0 auto;
                width: 540px;
                font 16px sans-serif;
                border-radius: 10px;
            }
            testarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label for="rotate-by">
                Rotate by:
                
                <input id="rotate-by" type="text" name="rot" value=0 />
                <br>
                <br>
                <label for="text">
                <textarea id="text" name="text"></textarea>
                <br>
            </label>
            
            <input type="submit" value="Submit Query"/>
        </form>

    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt(rot, text):
    rot = request.form['rotate-by']
    text = request.form['text']
    new_phrase = ""
    for letter in text:
        new_letter = rotate_character(letter, rot)
        new_phrase += new_letter
    return "<h1>" + new_phrase + "<h1>"

    
    
     
 


@app.route("/")
def index():
    return form

app.run()