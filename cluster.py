#TrueFalse

import matplotlib
import numpy
import astropy
import photutils

from astropy.io import fits
from matplotlib import pyplot
from matplotlib import cm
from matplotlib.colors import LogNorm
from photutils import datasets
from astropy.stats import sigma_clipped_stats
from photutils import daofind

def main():
    '''Call functions '''
    filename = 'testNGC884-001L.fit'
    fits_image(filename)
    filename = 'testNGC869-001L.fit'
    color_filters(filename)
    filename = 'testNGC884-001L.fit'
    star_detection(filename)


def open_fits(filename):
    '''Read fits file '''
    hdulist = fits.open(filename)
    hdulist.info()
    image_data = hdulist[0].data
    print type(image_data)
    print image_data.shape
    hdulist.close()
    return image_data


def fits_image(filename):
    '''Plot fits image '''
    array = open_fits(filename)
    print "Dimensions is", array.shape
    print "Data type is", array.dtype
    pyplot.imshow(array, norm=LogNorm())
    pyplot.xlim(1800, 2200)
    pyplot.ylim(1800, 2200)
    pyplot.colorbar()
    pyplot.legend()
    pyplot.title('Fits image')
    pyplot.xlabel('X-axis [pixels]')
    pyplot.ylabel('Y-axis [pixels]')
    pyplot.savefig('fits_image.pdf')
    pyplot.show()

def color_filters(filename):
    '''Color filters  in red, green en blue'''
    Image_data = open_fits(filename)
    filename = 'testNGC869-001R.fit'
    image_data_r = open_fits(filename)
    filename = 'testNGC869-001V.fit'
    image_data_g = open_fits(filename)
    filename = 'testNGC869-001B.fit'
    image_data_b = open_fits(filename)
    pyplot.figure(1)
    pyplot.suptitle('Color Filters')
    pyplot.subplot(221)
    pyplot.imshow(image_data_r, norm=LogNorm(), cmap=cm.Reds_r)
    pyplot.title('Red channel')
    pyplot.xlim(1900, 2100)
    pyplot.ylim(1900, 2100)
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(222)
    pyplot.imshow(image_data_g, norm=LogNorm(), cmap=cm.Greens_r)
    pyplot.title('Green channel')
    pyplot.xlim(1900, 2100)
    pyplot.ylim(1900, 2100)
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(223)
    pyplot.imshow(image_data_b, norm=LogNorm(), cmap=cm.Blues_r)
    pyplot.title('Blue channel')
    pyplot.xlim(1900, 2100)
    pyplot.ylim(1900, 2100)
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(224)
    pyplot.imshow(image_data, norm=LogNorm())
    pyplot.title('Full color')
    pyplot.xlim(1900, 2100)
    pyplot.ylim(1900, 2100)
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.savefig('color_filters.pdf')
    pyplot.show()

def star_detection(filename):
    ''' Detect stars, create scatter plot'''
    image_data = open_fits(filename)
    mean, median, std = sigma_clipped_stats(image_data, sigma=3.0, iters=5)
    print mean, median, std
    sources = daofind(image_data - median, fwhm=3.0, threshold=5.*std)
    print sources
    x_val = [x[1] for x in sources]
    y_val = [x[2] for x in sources]
    pyplot.imshow(image_data, norm=LogNorm())
    pyplot.scatter(x_val, y_val, color='k', marker='o', label='Detected stars')
    pyplot.xlim(1800, 2200)
    pyplot.ylim(1800, 2200)
    pyplot.colorbar()
    pyplot.legend()
    pyplot.title('Star detection')
    pyplot.xlabel('X-axis [pixels]')
    pyplot.ylabel('Y-axis [pixels]')
    pyplot.savefig('star_detection.pdf')
    pyplot.show()


if __name__=='__main__':
    main()
