
OPTIONS = [


    [
        "symbology" ,
        "integer",
        "Symbology to use (see section 5.7).",
        "BARCODE_CODE128",
    ]
,

    [
        "height",
        "integer",
        "Symbol height. [1]",
        50,
    ]
,
    [
        "whitespace_width",
        "integer",
        "Whitespace width.",
        0,
    ]
,
    [
        "border_width",
        "integer",
        "Border width.",
        0,
    ]
,
    [
        "output_options",
        "integer",
        "Binding or box parameters (see section 5.8). [2]",
        None ,
    ]
,
    [
        "fgcolour",
        "character string",
        "Foreground (ink) colour as RGB hexadecimal string. Must be 6 characters followed by terminating \0 character.",
        "000000",
    ]
,
    [
        "bgcolour",
        "character string",
        "Background (paper) colour as RGB hexadecimal string. Must be 6 characters followed by terminating \0 character.",
        "ffffff",
    ]
,
    [
        "outfile",
        "character string",
        "Contains the name of the file to output a resulting barcode symbol to. Must end in .png, .eps or .svg",
        "out.png",
    ]
,
    [
        "option_1",
        "integer",
        "Symbology specific options.",
        "(automatic)",
    ]
,
    [
        "option_2",
        "integer",
        "Symbology specific options.",
        "(automatic)",
    ]
,
    [
        "option_3",
        "integer",
        "Symbology specific options.",
        "(automatic)",
    ]
,
    [
        "scale",
        "float",
        "Scale factor for adjusting size of image.",
        "1.0",
    ]
,
    [
        "input_mode",
        "integer",
        "Set encoding of input data (see section 5.9)",
        "BINARY_MODE",
    ]
,
    [
        "primary",
        "character string",
        "Primary message data for more complex symbols.",
        "NULL",
    ]
,
    [
        "text",
        "unsigned character string",
        "Human readable text, which usually consists of the input data plus one or more check digits. Uses UTF-8 formatting.",
        "NULL",
    ]
,
    [
        "rows",
        "integer",
        "Number of rows used by the symbol or, if using barcode stacking, the row to be used by the next symbol.",
        "(output only)",
    ]
,
    [
        "width",
        "integer",
        "Width of the generated symbol.",
        "(output only)",
    ]
,
    [
        "encoding_data",
        "array of character strings",
        "Representation of the encoded data.",
        "(output only)",
    ]
,
    [
        "row_height",
        "array of integers",
        "Representation of the height of a row.",
        "(output only)",
    ]
,
    [
        "errtxt",
        "character string",
        "Error message in the event that an error occurred.",
        "(output only)",
    ]
,
    [
        "bitmap",
        "pointer to character array",
        "Pointer to stored bitmap image.",
        "(output only)",
    ]
,
    [
        "bitmap_width",
        "integer",
        "Width of stored bitmap image (in pixels).",
        "(output only)",
    ]
,
    [
        "bitmap_height",
        "integer",
        "Height of stored bitmap image (in pixels).",
        "(output only)",
    ]
]


if __name__ == "__main__":
    for option in OPTIONS:
        print(option)
