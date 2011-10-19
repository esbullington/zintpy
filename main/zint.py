#!/usr/bin/env python
# coding: utf8
# Copyright Eric S. Bullington, 2011
# Licensed under MIT and GPLv3
# Python wrapper for libzint - the open source barcode library
# http://sourceforge.net/projects/zint/

from ctypes import *

class zint_render_line(Structure):
    pass
zint_render_line._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('length', c_float),
    ('width', c_float),
    ('next', POINTER(zint_render_line)),
]
class zint_render_string(Structure):
    pass
zint_render_string._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('fsize', c_float),
    ('width', c_float),
    ('length', c_int),
    ('text', POINTER(c_ubyte)),
    ('next', POINTER(zint_render_string)),
]
class zint_render_ring(Structure):
    pass
zint_render_ring._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('radius', c_float),
    ('line_width', c_float),
    ('next', POINTER(zint_render_ring)),
]
class zint_render_hexagon(Structure):
    pass
zint_render_hexagon._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('next', POINTER(zint_render_hexagon)),
]

class zint_render(Structure):
    pass
zint_render._fields_ = [
    ('width', c_float),
    ('height', c_float),
    ('lines', POINTER(zint_render_line)),
    ('strings', POINTER(zint_render_string)),
    ('rings', POINTER(zint_render_ring)),
    ('hexagons', POINTER(zint_render_hexagon)),
]


class zint_symbol(Structure):
    pass
zint_symbol._fields_ = [
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
    ('rendered', POINTER(zint_render)),
]

#new_symbol = zint_symbol(56,400,0,0,0,"000000","ffffff","eric.png",1.0,0,0,0,0,0,,0,0,0,0,0,0,0,0,0,0)

class Zint:
    def render(self,symbol=56,scl=3,ht=50,opt2=3,opt1=3,msg="hello watson",ww=0,bw=0,output=0,foreground="000000",background="ffffff",file_name="out.png"):
        zint = CDLL("/usr/lib/libzint.so")
        zint.ZBarcode_Create.restype = POINTER(zint_symbol)
        my_symbol = zint.ZBarcode_Create()
        my_symbol.contents.symbology = symbol
        my_symbol.contents.scale = scl
        message = msg
        my_symbol.contents.whitespace_width = ww
        my_symbol.contents.border_width = bw
        my_symbol.contents.output_options = output
        my_symbol.contents.fgcolour = foreground
        my_symbol.contents.bgcolour = background
        my_symbol.contents.outfile = file_name
        return zint.ZBarcode_Encode_and_Print(my_symbol,(c_char_p(message)),c_int(0),c_int(0))
