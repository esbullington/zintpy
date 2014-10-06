#!/usr/bin/env python
# coding: utf8
# Copyright Eric S. Bullington, 2011
# Licensed under MIT and GPLv3
# Python wrapper for libzint - the open source barcode library
# http://sourceforge.net/projects/zint/

from optparse import OptionParser
from ctypes import *
from zint import Zint


#new_symbol = zint_symbol(56,400,0,0,0,"000000","ffffff","eric.png",1.0,0,0,0,0,0,,0,0,0,0,0,0,0,0,0,0)

def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage)
    parser.add_option("-s", "--symbology", dest="symbology", type="int", help="Sets barcode symbology")
    parser.add_option("-m", "--message", dest="message", type="string", help="Sets barcode message")
    (options, args) = parser.parse_args()
    zint = Zint(symbology=options.symbology)
    zint.render(options.message)


if __name__ == "__main__":
    main()
