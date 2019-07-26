from flask import Flask
from app.matrixController.controller import Controller
from threading import Thread

def launchController(controller):
    controller.begin()

if __name__ == '__main__':
    controller = Controller(useVirtualMatrix=True)
    flaskApp = Flask(__name__)
    controllerThread = Thread(target=launchController, args=(controller,))
    controllerThread.start()
    flaskApp.run(host='0.0.0.0')
