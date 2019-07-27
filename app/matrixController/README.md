
# LED Matrix Controller

This is a simple python program for accepting https
requests containing animation data and controlling
an LED matrix through GPIO to display the animations.

## Installation
You should probably create a virtual environment in this directory with

```
virtualenv matrixenv
```

and activate it with
```./matrixenv/Scripts/activate```
with the appropriate file extension for the activation script.

Run
```
pip -r requirements.txt
```
to install all dependencies on
a raspberry pi. On other platforms, instead use
```
pip -r requirements-no-pi.txt
```


Run tests with
```
python -m pytest -v
```


To start the controller using a virtual matrix instead of the
physical one, use
```
python controller.py --virtual
```

## Explanation

See the [explanation for matrix devices to get started](./devices/README.md).

TODO rest
