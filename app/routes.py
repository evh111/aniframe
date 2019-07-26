from flask import render_template, request, url_for
from app import app
from json import dumps


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animation', methods=['POST'])
def animation():
    print(request.get_json(force=True))
    return '', 200
