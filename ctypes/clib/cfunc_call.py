#!/usr/bin/python3

import ctypes;
import pathlib;

if __name__ == "__main__":

    libname = pathlib.Path().absolute() / "out/cfunc.so"
    print("Loading library: %s" % libname)

    c_lib = ctypes.CDLL(libname)

    # Input parameters treated as int by default
    # in other case use c_float() and etc conversions
    a = 1
    b = 2

    print("Calling csum(): %u %u" % (a, b));
    result = c_lib.csum(a, b)

    print("csum result: %u" % result);
