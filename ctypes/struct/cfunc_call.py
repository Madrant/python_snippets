#!/usr/bin/python3

from ctypes import *;
import pathlib;

class message_T(Structure):
    _fields_ = [
        ("uid",    c_uint),
        ("time",   c_uint),
        ("a",      c_char),
        ("b",      c_char),
        ("c",      c_char),
        ("d",      c_char)
    ]

    # display structure content using print()
    def __str__(self):
        str = ""

        for field in self._fields_:
            str += (
                "%s: %s " %
                (field[0], getattr(self, field[0]))
            )

        return str

if __name__ == "__main__":

    libname = pathlib.Path().absolute() / "out/cfunc.so"
    print("Loading library: %s" % libname)

    c_lib = CDLL(libname)

    c_process = c_lib.process
    c_process.argtypes = [POINTER(message_T)]
    c_process.restype = c_int;

    print("Calling process()");

    message = message_T(1, 2, b'a', b'b', b'c', b'd')
    print(message)

    result = c_process(byref(message))

    print("process() result: %u" % result);
