#!/usr/bin/python3

from ctypes import *
import pathlib
import random

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

    # Pass a struct to function by pointer
    c_process = c_lib.process
    c_process.argtypes = [POINTER(message_T)]
    c_process.restype = c_int;

    print("Calling process()");

    message = message_T(1, 2, b'a', b'b', b'c', b'd')
    print(message)

    result = c_process(byref(message))

    print("process() result: %u" % result);

    # Pass an array of structs to function by pointer
    messages = 3

    c_process_array = c_lib.process_array
    c_process_array.argtypes = [POINTER(message_T * messages), c_int]
    c_process_array.restype = c_int;

    # Create an array of ctypes structs
    message_array_pointer = (message_T * messages)(
        message_T(1, 3, b'a', b'b', b'c', b'd'),
        message_T(2, 2, b'a', b'b', b'c', b'd'),
        message_T(3, 1, b'a', b'b', b'c', b'd')
    )

    for i in range(messages):
        print(message_array_pointer[i])

    print("Calling process_array()");

    result = c_process_array(message_array_pointer, messages)

    # Convert ctypes array of structs to python list
    messages_list = [message_array_pointer[i] for i in range(messages)]

    print("process() result: %u" % result)
    for m in messages_list: print(m)
