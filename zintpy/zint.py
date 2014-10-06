#!/usr/bin/env python
# coding: utf8
# Copyright Eric S. Bullington, 2011, 2012, 2013
# Licensed under BSD
# Python wrapper for libzint - the open source barcode library
# http://sourceforge.net/projects/zint/

from ctypes import *


class ZintRenderLine(Structure):
    pass
    
ZintRenderLine_fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('length', c_float),
    ('width', c_float),
    ('next', POINTER(ZintRenderLine)),
]


class ZintRenderString(Structure):
    pass


ZintRenderString._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('fsize', c_float),
    ('width', c_float),
    ('length', c_int),
    ('text', POINTER(c_ubyte)),
    ('next', POINTER(ZintRenderString)),
]


class ZintRenderRing(Structure):
    pass


ZintRenderRing._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('radius', c_float),
    ('line_width', c_float),
    ('next', POINTER(ZintRenderRing)),
]


class ZintRenderHexagon(Structure):
    pass


ZintRenderHexagon._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('next', POINTER(ZintRenderHexagon)),
]


class ZintRender(Structure):
    pass


ZintRender._fields_ = [
    ('width', c_float),
    ('height', c_float),
    ('lines', POINTER(ZintRenderLine)),
    ('strings', POINTER(ZintRenderString)),
    ('rings', POINTER(ZintRenderRing)),
    ('hexagons', POINTER(ZintRenderHexagon)),
]


class ZintSymbol(Structure):
    pass


ZintSymbol._fields_ = [
    ('symbology', c_int),
    ('height', c_int),
    ('whitespace_width', c_int),
    ('border_width', c_int),
    ('output_options', c_int),
    ('fgcolour', c_char * 10),
    ('bgcolour', c_char * 10),
    ('outfile', c_char * 256),
    ('scale', c_float),
    ('option_1', c_int),
    ('option_2', c_int),
    ('option_3', c_int),
    ('show_hrt', c_int),
    ('input_mode', c_int),
    ('text', c_ubyte * 128),
    ('rows', c_int),
    ('width', c_int),
    ('primary', c_char * 128),
    ('encoded_data', c_ubyte * 143 * 178),
    ('row_height', c_int * 178),
    ('errtxt', c_char * 100),
    ('bitmap', c_char_p),
    ('bitmap_width', c_int),
    ('bitmap_height', c_int),
    ('rendered', POINTER(ZintRender)),
]


class Zint:

    def __init__(self, 
            symbology=56, 
            scale=3, height=50, 
            option_1=3, 
            option_2=3,
            whitespace_width=0,
            border_width=0,
            output_options=0,
            fgcolour="000000",
            bgcolour="ffffff",
            outfile="out.png"):
        self.zint = CDLL("/usr/local/lib/libzint.so")
        self.zint.ZBarcode_Create.restype = POINTER(ZintSymbol)
        self.symbol = self.zint.ZBarcode_Create()
        self.symbol.contents.symbology = symbology
        self.symbol.contents.scale = scale
        self.symbol.contents.whitespace_width = whitespace_width
        self.symbol.contents.border_width = border_width
        self.symbol.contents.output_options = output_options
        self.symbol.contents.fgcolour = fgcolour
        self.symbol.contents.bgcolour = bgcolour
        self.symbol.contents.outfile = outfile

    def render(self, message):
        return self.zint.ZBarcode_Encode_and_Print(self.symbol, (c_char_p(message)),c_int(0),c_int(0))
