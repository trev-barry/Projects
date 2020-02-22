# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
#--------------------------------------------------------------
# start the clock
start = time.time()

# functions to be used
orb = cv2.ORB_create() # creating the orb func that finds features
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
#--------------------------------------------------------------

# reading in the images (must be a jpg)
star_map = cv2.imread('X24546ACK.jpg',0) # <---- STAR CHART FILE
telescope_output = cv2.imread('star_test_1.jpg',0)
#--------------------------------------------------------------
kp1, des1 = orb.detectAndCompute(star_map,None)
kp2, des2 = orb.detectAndCompute(telescope_output,None)

matches = bf.match(des1, des2)

#sortes by least likely of match to most likely
matches = sorted(matches, key = lambda x:x.distance)
#--------------------------------------------------------------
# drawing out the comparison picture
final_image = cv2.drawMatches(star_map,kp1, telescope_output,kp2, matches[:5],None,flags=2)
plt.imshow(final_image)
plt.show()
#--------------------------------------------------------------
# end the clock
end = time.time()
print('Total time:',end - start)

# source code
# https://www.youtube.com/watch?v=UquTAf_9dVA
# https://github.com/deprecated/fits2image (FIT converter code)
# https://www.files-conversion.com/image/fits
