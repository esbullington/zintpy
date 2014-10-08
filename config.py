[main]

#Symbology to use (see section 5.7).
symbology: BARCODE_CODE128
#Symbol height. [1]
height: 50
#Whitespace width.
whitespace_width: 0
#Border width.
border_width: 0
#Binding or box parameters (see section 5.8). [2]
output_options: None
#Foreground (ink) colour as RGB hexadecimal string. Must be 6 characters followed by terminating   character.
fgcolour: 000000
#Background (paper) colour as RGB hexadecimal string. Must be 6 characters followed by terminating   character.
bgcolour: ffffff
#Contains the name of the file to output a resulting barcode symbol to. Must end in .png, .eps or .svg
outfile: out.png
#Symbology specific options.
option_1: 
#Symbology specific options.
option_2: 
#Symbology specific options.
option_3: 
#Scale factor for adjusting size of image.
scale: 1.0
#Set encoding of input data (see section 5.9)
input_mode: BINARY_MODE
#Primary message data for more complex symbols.
primary: NULL
#Human readable text, which usually consists of the input data plus one or more check digits. Uses UTF-8 formatting.
text: NULL
#Number of rows used by the symbol or, if using barcode stacking, the row to be used by the next symbol.
rows: 
#Width of the generated symbol.
width: 
#Representation of the encoded data.
encoding_data: 
#Representation of the height of a row.
row_height: 
#Error message in the event that an error occurred.
errtxt: 
#Reference to stored bitmap image.
bitmap: 
#Width of stored bitmap image (in pixels).
bitmap_width: 
#Height of stored bitmap image (in pixels).
bitmap_height: 
