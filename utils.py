# scrcpy

import pyscreenshot
from PIL import Image

import numpy as np


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float"))**2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def image_loader():
    ads_complete = Image.open('img/ads_complete.png')
    ad_not_ready_1 = Image.open('img/ad_not_ready_1.png')
    ad_ready_1 = Image.open('img/ad_ready_1.png')
    ad_ready_2 = Image.open('img/ad_ready_2.png')
    imgs = (ads_complete, ad_not_ready_1, ad_ready_1, ad_ready_2)
    return imgs


def check_ad_ready(ad_ready_1):
    im = pyscreenshot.grab()
    d = mse(np.array(im), np.array(ad_ready_1))
    if d < 1000:
        return True
    else:
        return False


def check_ad_screen(ad_ready_1, ad_not_ready_1):
    im = pyscreenshot.grab()
    d_0 = mse(np.array(im), np.array(ad_ready_1))
    d_1 = mse(np.array(im), np.array(ad_not_ready_1))
    if d_1 < 3000 or d_0 < 3000:
        return True
    else:
        return False


if __name__ == '__main__':
    import time
    ad_finished, ad_not_ready_1, ad_ready_1, ad_ready_2 = image_loader()

    while True:
        im = pyscreenshot.grab()
        d = mse(np.array(im), np.array(ad_ready_1))
        print(d)
        time.sleep(5)
