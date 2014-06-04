Welcome to imread's documentation!
==================================

Imread is a very simple libray. It has three functions

imread
    Reads an image from disk
imread_multi
    Reads multiple images from disk (only for file formats that support
    multiple images)
imwrite
    Save an image to disk

That's it.

Imread is to be used with computer vision & image processing packages:

- `mahotas <http://luispedro.org/software/mahotas>`__
- `scikit-image <http://scikit-image.org/>`__
- `OpenCV <http://opencv.willowgarage.com/wiki/>`__


Imread grew out of frustration at current image-loading solutions in Python, in
either my own packages, e.g. [`mahotas <http://mahotas.rtfd.org>`__], or in those
written by others, such as [`scikit-image <http://scikit-image.org>`__, for example].

Imread’s relationship with numpy is very contained, and thus could be easily
repurposed as an image-loader for use in other frameworks – even other programming
languages.

Citation
--------

This package is an off-shoot of mahotas. As it currently does not have its
own publication, you are asked to cite the parent package. If you use
imread-mahotas on a scientific publication, please cite:

    **Luis Pedro Coelho** Mahotas: Open source software for scriptable computer
    vision in Journal of Open Research Software, vol 1, 2013. [`DOI
    <http://dx.doi.org/10.5334/jors.ac>`__]


In Bibtex format::

    @article{mahotas,
        author = {Luis Pedro Coelho},
        title = {Mahotas: Open source software for scriptable computer vision},
        journal = {Journal of Open Research Software},
        year = {2013},
        doi = {http://dx.doi.org/10.5334/jors.ac},
        month = {July},
        volume = {1}
    }


INSTALL
~~~~~~~

On Windows, you can also just download a pre-built package from `C. Gohlke's
repository <http://www.lfd.uci.edu/~gohlke/pythonlibs/#imread>`__

To compile on debian/ubuntu::

    sudo apt-get install libpng12-dev libtiff4-dev libwebp-dev
    sudo apt-get install xcftools

To compile on Mac::

    sudo port install libpng tiff webp

Either way, you can then install::

    pip install imread


Contents:

.. toctree::
   :maxdepth: 2

   readme
   formats
   non-python
   history

Bug Reports
~~~~~~~~~~~

Please report any bugs either on `github
<http://github.com/luispedro/imread>`__ or by email to luis@luispedro.org

If you have a test case where are not sure of whether imread is behaving
correctly, you can discuss this on the `pythonvision mailing list
<https://groups.google.com/forum/?fromgroups#!forum/pythonvision>`__

If at all possible, include a small image as a test case.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

