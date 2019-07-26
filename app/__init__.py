from app import routes
from flask import Flask, send_from_directory

app = Flask(__name__, static_url='path')
