from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.1.88')

from app import routes

