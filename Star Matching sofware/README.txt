LIST OF FILES

This file includes two pieces of python code I created as a side project for the MSU Observatory. Along with this code several pictures taken by the observatory are included. This includes an example star chart that is used for comparison to the example star image that was produced by the MSU Observatory. These two images are used by the code to preform calibrations on the telescope and aid in speeding up the calibration processes at the beginning of the observing time.
------------------------------------------------------------------------------------------------------------------------------
ABOUT THIS CODE

This program runs on python and was created for the purpose of identifying and matching star charts to images produced at the MSU Observatory. At the observatory we are tasked with finding a star to observe for the night using FIT images. We first find the location of the star from an image database that produces an image of our target star along with surround stars for reference. This image we use to compare to the images that the telescope produces. This process is used as a check against the MSU telescope to make sure that our target star is perfectly centered for image capturing. The image_convert.py is a python program that converts the FIT images produced by the telescope and converts them into jpegs. This is not my own, but code slightly modified that I found from https://github.com/deprecated/fits2image. The second python code star_matchin.py is a code that takes in two images, one produced by the observatory and an image from our star charts. This code then finds similarities between the two and and produces a list of matches between the two. This code was produced in the hopes that it would speed up the calibration process at the beginning of each night. The code sources/inspirations are listed at the bottom of star_matching.py
------------------------------------------------------------------------------------------------------------------------------
LIBRARIES USED

numpy
sys
astropy.io
pyfits
PIL
cv2
matplotlib
time
