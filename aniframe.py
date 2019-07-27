from flask import Flask
from flask import render_template
from flask import request
from app.matrixController.controller import Controller

from threading import Thread
from loto import LockoutTagout


if __name__ == '__main__':
    # The general idea is to set up flask's routes while 
    # giving them access to the controller object.
    # Then, we start a thread for the controller
    # to run its loop independently of the flask thread.
    # the flask routes will use a mutex to make sure
    # they are not writing to the frame data while
    # it's being rendered.

    flaskApp = Flask(__name__)

    def launchController(controller):
        controller.begin()

    @LockoutTagout('matrixData')
    def updateData(data):
        controller.updateData(data)


    @flaskApp.route('/')
    def index():
        return render_template('index.html')


    @flaskApp.route('/animation', methods=['POST'])
    def animation():
        updateData(request.get_json(force=True))
        return '', 200

    # How do we want to set this flag? Using argparse? Click?
    controller = Controller(useVirtualMatrix=True)
    controllerThread = Thread(target=launchController, args=(controller,))
    controllerThread.daemon = True # kill thread if parent dies
    controllerThread.start()

    flaskApp.run(host='0.0.0.0')
