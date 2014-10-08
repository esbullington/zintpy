
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


SYMBOLOGIES = {
    "1": "Code 11",
    "2": "Standard Code 2 of 5",
    "3": "Interleaved 2 of 5",
    "4": "Code 2 of 5 IATA",
    "6": "Code 2 of 5 Data Logic",
    "7": "Code 2 of 5 Industrial",
    "8": "Code 3 of 9 (Code 39)",
    "9": "Extended Code 3 of 9 (Code 39+)",
    "13": "EAN",
    "16": "GS1-128 (UCC.EAN-128)",
    "18": "Codabar",
    "20": "Code 128 (automatic subset switching)",
    "21": "Deutshe Post Leitcode",
    "22": "Deutshe Post Identcode",
    "23": "Code 16K",
    "24": "Code 49",
    "25": "Code 93",
    "28": "Flattermarken",
    "29": "GS1 DataBar-14",
    "30": "GS1 DataBar Limited",
    "31": "GS1 DataBar Extended",
    "32": "Telepen Alpha",
    "34": "UPC A",
    "37": "UPC E",
    "40": "PostNet",
    "47": "MSI Plessey",
    "49": "FIM",
    "50": "LOGMARS",
    "51": "Pharmacode One-Track",
    "52": "PZN",
    "53": "Pharmacode Two-Track",
    "55": "PDF417",
    "56": "PDF417 Truncated",
    "57": "Maxicode",
    "58": "QR Code",
    "60": "Code 128 (Subset B)",
    "63": "Australia Post Standard Customer",
    "66": "Australia Post Reply Paid",
    "67": "Australia Post Routing",
    "68": "Australia Post Redirection",
    "69": "ISBN (EAN-13 with verification stage)",
    "70": "Royal Mail 4 State (RM4SCC)",
    "71": "Data Matrix",
    "72": "EAN-14",
    "75": "NVE-18",
    "76": "Japanese Postal Code",
    "77": "Korea Post",
    "79": "GS1 DataBar-14 Stacked",
    "80": "GS1 DataBar-14 Stacked Omnidirectional",
    "81": "GS1 DataBar Expanded Stacked",
    "82": "PLANET",
    "84": "MicroPDF417",
    "85": "USPS OneCode",
    "86": "Plessey Code",
    "87": "Telepen Numeric",
    "89": "ITF-14",
    "90": "Dutch Post KIX Code",
    "92": "Aztec Code",
    "93": "DAFT Code",
    "97": "Micro QR Code",
    "98": "HIBC Code 128",
    "99": "HIBC Code 39",
    "102": "HIBC Data Matrix",
    "104": "HIBC QR Code",
    "106": "HIBC PDF417",
    "108": "HIBC MicroPDF417",
    "112": "HIBC Aztec Code",
    "128": "Aztec Runes",
    "129": "Code 32",
    "130": "Composite Symbol with EAN linear component",
    "131": "Composite Symbol with GS1-128 linear component",
    "132": "Composite Symbol with GS1 DataBar-14 linear component",
    "133": "Composite Symbol with GS1 DataBar Limited component",
    "134": "Composite Symbol with GS1 DataBar Extended component",
    "135": "Composite Symbol with UPC A linear component",
    "136": "Composite Symbol with UPC E linear component",
    "137": "Composite Symbol with GS1 DataBar-14 Stacked component",
    "138": "Composite Symbol with GS1 DataBar-14 Stacked Omnidirectional component",
    "139": "Composite Symbol with GS1 DataBar Expanded Stacked component",
    "140": "Channel Code",
    "141": "Code One",
    "142": "Grid Matrix",
}

if __name__ == "__main__":
    for option in OPTIONS:
        print(option)

