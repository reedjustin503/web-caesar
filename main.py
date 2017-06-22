from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['Debug'] = True



form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
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
    <div contentEditable="true">
      <form action='/' method='post'>
        <label for='rotateby'>Rotate by:</label>
        <input id='rotateby', type='text', name='rotateby', placeholder='0'/>

        <label for='text'></label>
        <textarea type='text', name='text', placeholder='place text here'>{0}</textarea>
        <input type='submit' value='Submit Query' />



      </form>
    </div>
    </body>
"""

@app.route("/")
def index():
    return form.format("")


@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form[('rotateby')])
    text = request.form[('text')]


    cryptic = rotate_string(text, rot)
    return '<h1>' + form.format(cryptic) + '</h1>'



app.run()
