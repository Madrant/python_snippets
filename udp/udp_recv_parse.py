#!/usr/bin/python3

import socket
import struct

from ctypes import *

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
    ip = "0.0.0.0"
    port = 31337

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Listen on %s: %u" % (ip, port))
    sock.bind((ip, port))

    while True:
        data, addr = sock.recvfrom(64)

        print("Packet size: %u data: %s" % (len(data), data.hex()))

        # Use struct.unpack format characters:
        #
        # Byte order:
        # @ - native with native alignment
        # = - native no alignment
        # < - little-endian
        # > - big-endian
        # ! - network (big-endian)
        #
        # Format characters (not complete list):
        # x - padding
        # c - char (1)
        # B - unsigned char (1)
        # H - unsigned short (2)
        # I - unsigned int (4)
        # f - float (4)
        # d - double (8)
        format = '!IIBBBB'

        try:
            (uuid, time, a, b, c, d) = struct.unpack(format, data)
        except struct.error:
            print(
                "Cannot unpack array: %u bytes must be: %u" %
                (len(data), struct.calcsize(format))
            )
            continue

        print(uuid, time, a, b, c, d)

        message = message_T(uuid, time, a, b, c, d)
        print(message)
