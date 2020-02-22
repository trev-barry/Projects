import numpy as np
import sys
# convert fits to jpg
try:
    from astropy.io import fits
except ImportError:
    import pyfits as fits
from PIL import Image

# Read command line arguments
try:
    fitsfilename = sys.argv[1]
    vmin, vmax = float(sys.argv[2]), float(sys.argv[3])
#except IndexError:
#    sys.exit('Usage: ' + sys.argv[0] + ' FITSFILENAME VMIN VMAX')

# Try to read data from first HDU in fits file
data = fits.open('run1_2019_07_08_V339_Del_120s_Clear-0003.fit')[0].data # <----- PUT FIT FILE HERE
# If nothing is there try the second one
if data is None:
    data = fits.open('run1_2019_07_08_V339_Del_120s_Clear-0003.fit')[1].data # <----- PUT FIT FILE HERE

# Clip data to brightness limits
data[data > vmax] = vmax
data[data < vmin] = vmin
# Scale data to range [0, 1]
data = (data - vmin)/(vmax - vmin)
# Convert to 8-bit integer
data = (255*data).astype(np.uint8)
# Invert y axis
data = data[::-1, :]

# Create image from data array and save as jpg
image = Image.fromarray(data, 'L')
imagename = fitsfilename.replace('.fits', '.jpg')
image.save(imagename)
