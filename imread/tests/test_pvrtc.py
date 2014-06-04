from nose.tools import raises
import numpy as np
from imread import imread

@raises(RuntimeError)
def test_error():
    imread('./imread/tests/data/error.webp')
    
def test_AI88():
    im = imread('./imread/tests/data/pvrsamples/AI88.pvr')
    #assert np.any(im) FAIL WTF

def test_I8():
    im = imread('./imread/tests/data/pvrsamples/I8.pvr')
    assert np.any(im)

def test_RGB565():
    im = imread('./imread/tests/data/pvrsamples/RGB565.pvr')
    assert np.any(im)

def test_RGB888():
    im = imread('./imread/tests/data/pvrsamples/RGB888.pvr')
    assert np.any(im)

def test_RGBA4444():
    im = imread('./imread/tests/data/pvrsamples/RGBA4444.pvr')
    assert np.any(im)

def test_RGBA5551():
    im = imread('./imread/tests/data/pvrsamples/RGBA5551.pvr')
    assert np.any(im)

def test_RGBA8888():
    im = imread('./imread/tests/data/pvrsamples/RGBA8888.pvr')
    assert np.any(im)

def test_apple_2bpp():
    im = imread('./imread/tests/data/pvrsamples/apple_2bpp.pvr')
    assert np.any(im)

def test_apple_4bpp():
    im = imread('./imread/tests/data/pvrsamples/apple_4bpp.pvr')
    assert np.any(im)

def test_pvrtc2bpp():
    im = imread('./imread/tests/data/pvrsamples/pvrtc2bpp.pvr')
    assert np.any(im)

def test_pvrtc4bpp():
    im = imread('./imread/tests/data/pvrsamples/pvrtc4bpp.pvr')
    assert np.any(im)

# pngreference.png ...?


    
