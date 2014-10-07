##ZintPy

ZintPy is a Python wrapper for the libzint barcode-encoding library, developed by Robin Stuart and other contributors as part of the [Zint Barcode Generator project](http://sourceforge.net/projects/zint/).

This package is still under active development and may not yet work on all listed platforms.

Features
----
Support for over 50 symbologies, including:
* Code 128
* Data Matrix
* USPS OneCode
* EAN-128
* UPC/EAN
* ITF
* QR Code
* Code 16k
* PDF417
* MicroPDF417
* LOGMARS
* Maxicode
* GS1 DataBar
* Aztec
* Composite Symbols

Version
----

0.2.0

Installation
----

To install this module, please type the following:

`python setup.py install zintpy` or `pip install zintpy`

Dependencies
----

####Windows
For Windows, this module requires the Zint Barcode Generator to be installed:

http://sourceforge.net/projects/zint/files/zint/2.4.3/

####Linux
For Linux, all necessary dependencies are installed automatically with `python setup.py install` or `pip install zintpy`

####OSX
For OSX, a version of Zint is evidently available via homebrew. This should install the necessary `dylib` although this method is so far untested:

`brew install zint`

Examples
----
TODO

Roadmap
----

License
----
####ZintPy Python bindings
Copyright (c) 2011-2014 Eric S. Bullington

####libzint - the open source barcode library
Copyright (c) 2008-2014 Robin Stuart and contributors

Both the libzint library used in this package and the Python package itself are licensed under the [3-clause BSD license](http://opensource.org/licenses/BSD-3-Clause).
