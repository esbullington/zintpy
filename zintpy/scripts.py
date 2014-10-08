#!/usr/bin/env python
# coding: utf8

import pkg_resources  # part of setuptools
import ConfigParser
import os
from optparse import OptionParser
from ctypes import *
from zint import Zint
from constants import SYMBOLOGIES
from six import iteritems


VERSION = pkg_resources.require("zintpy")[0].version

def search_symbologies(option, opt, value, parser):
    search_success = False
    for key, val in iteritems(SYMBOLOGIES):
        if value.lower() in val.lower():
            search_success = True
            print("Zint Code: {:<4} Symbology: {}".format(key, val))
    if not search_success:
        print("No matching Zint symbology found.")
    print("")


def list_symbologies(option, opt, value, parser):
    for key, val in iteritems(SYMBOLOGIES):
        print("Zint Code: {:<4} Symbology: {}".format(key, val))
    print("")


def parse_config(option, opt, value, parser):
    with open(value) as f:
        config = ConfigParser.ConfigParser()
        config.readfp(f)
        symbology = config.get("main", "symbology")
        print("Symbology is: {}".format(symbology))

def main():
    usage = "usage: %prog [options] symbology message"
    desc="""To view available barcodes, pass the '-l' option: %prog -l"""
    parser = OptionParser(usage,  version="%prog " + VERSION, description=desc)
    parser.add_option("-l", "--list-symbologies", action="callback", callback=list_symbologies, help="Lists all available symbologies and their respective Zint codes")
    parser.add_option("-k", "--symbology-keyword", action="callback", callback=search_symbologies, type="str", help="Performs a keyword search for symbologies and their respective Zint codes")
    # parser.add_option("-c", "--config-file", action="callback", callback=parse_config, type="str", help="Pass in name and location of configuration file (see config_example.py for examples")
    (options, args) = parser.parse_args()
    if len(args) < 2:
        print('zintpy requires a symbology and message to produce a barcode. ex: zintpy 59 "this is a qr code"\n')
        return False
    symbology = int(args[0])
    message = args[1]
    zint = Zint(symbology=symbology, height=options.height)
    zint.render(message)


if __name__ == "__main__":
    main()
