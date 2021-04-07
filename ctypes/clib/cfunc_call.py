#!/usr/bin/python3

import pathlib
import ctypes

class c_struct(ctypes.Structure):
    _fields_ = [
        ("uid",    ctypes.c_uint),
        ("time",   ctypes.c_uint),
        ("a",      ctypes.c_char),
        ("b",      ctypes.c_char),
        ("c",      ctypes.c_char),
        ("d",      ctypes.c_char)
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

    c_lib = ctypes.CDLL(libname)

    # Define and call simple function:
    c_sum = c_lib.sum
    c_sum.argtypes = [ctypes.c_int, ctypes.c_int]
    c_sum.restype = ctypes.c_int

    # Input parameters treated as int by default
    # in other case use c_float() and etc conversions
    a = 1
    b = 2

    print("Calling csum(): %u %u" % (a, b))
    result = c_sum(a, b)
    print("csum result: %u" % result)

    # Define and call function that consumes 'const char*'
    c_hello = c_lib.hello
    c_hello.argtypes = [ctypes.c_char_p]

    name = "User"
    b_name = name.encode('utf-8')
    c_name = ctypes.c_char_p(b_name)

    print("Calling hello(): %s" % (name))
    c_hello((c_name))

    # Define and call functions that get parameter by reference/pointer
    c_print_struct = c_lib.print_struct
    c_print_struct.argtypes = [ctypes.POINTER(c_struct)]

    struct = c_struct(1, 2, b'a', b'b', b'c', b'd')

    print("Calling print_struct()")
    print(struct)

    c_print_struct(ctypes.byref(struct))
