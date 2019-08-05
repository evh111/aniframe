from app import matrixDataTag
import argparse
from threading import Thread
from flask import Flask, render_template, request

from app.matrixController.controller import Controller
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

    @LockoutTagout(matrixDataTag)
    def updateData(data):
        controller.updateData(data)

    @flaskApp.route('/')
    def index():
        return render_template('index.html')

    @flaskApp.route('/animation', methods=['POST'])
    def animation():
        updateData(request.get_json(force=True))
        return '', 200

    # argparse to make virtual matrix optional
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--virtual',
                        help='Enable the virtual matrix', action='store_true')

    args = parser.parse_args()
    virtual = args.virtual

    controller = Controller(useVirtualMatrix=args.virtual)
    controllerThread = Thread(target=launchController, args=(controller,))
    controllerThread.daemon = True  # Kill thread if parent dies
    controllerThread.start()

    flaskApp.run(host='0.0.0.0')
