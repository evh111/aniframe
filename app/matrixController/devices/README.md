# Matrix Devices

The classes in this directory represent various matrix devices
as well as helper classes such as `Pixels`.

`MatrixDevices` can be the real physical matrix device, or they can be
the virtual matrix device used for debugging. You can also implement your
own. The interface is compliant with the description
of the
[LED RGB matrix from adafruit](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/how-the-matrix-works).

## Overview

A matrix device consists of many pixels that we write 3 bits of data to.
The device is broken down into sections; the first section is the first
row from the top and the first row from the center.
For example, the first section of a 16x32 matrix would be the starred portion here:

```
********************************
--------------------------------
--------------------------------
--------------------------------
--------------------------------
--------------------------------
--------------------------------
--------------------------------
********************************
--------------------------------
--------------------------------
--------------------------------
--------------------------------
--------------------------------
--------------------------------
--------------------------------

```

The second section would be the second row from the top and the second from the middle,
etc...

The matrix expects a controller to
write 3 bits to the **A**, **B**, and **C** pins in order to
select a section to write to.

```
bit pattern:     |  000, 001, 010, 011, 100, 101, 111
section number:  |  0    1    2    3    4    5    6
```

Next, we bring the `LAT` pin and the `OE` pin low to prepare the matrix's
shift register to receive RGB data.

Then, we write 3 of color data to the `R1`, `G1`, and `B1` pins to color
a pixel on the top half. Then we write 3 bits to `R2`, `G2`, and `B2` to
color the bottom half's pixel. Then, we write to the `CLK` pin
to move to the next column.

After we have written all data for this section, we write to the `LAT` pin
to make the matrix display the data we just wrote to the current section.
We also need to pull the `OE` (output enable) pin back high.

We can repeat the process while incrementing the section address to
draw a whole frame.

## Interface

Matrix devices will all support the following API
by inheriting from the `MatrixDevice` abstract base class:

```
selectSection(section)
writeTopPixel(pixel)
writeBottomPixel(pixel)
clock()
latch()
```
