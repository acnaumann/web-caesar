from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin 0 auto;
                width: 540px;
                font 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method='POST'>
            <label for="/rot" >
                Rotate by:
                <input  type="text" name='rot' value=0 />
            </label>
                <br>
                <br>
            <label >
                <textarea name="text">{0}</textarea>
                <br>
            </label>
            
            <input type="submit" value="Submit Query"/>
        </form>

    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    rotated_string = rotate_string(text, int(rot))
    return "<h1>" + form.format(rotated_string) + "<h1>"


@app.route("/")
def index():
    empty_string = ''
    return form.format(empty_string)

app.run()