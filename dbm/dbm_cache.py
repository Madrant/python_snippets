#!/usr/bin/python3

import dbm
import hashlib

if __name__ == "__main__":

    # Setup db input
    name = "Max"

    print("Input: %s" % (name))

    # Prepare output
    output = ""

    # Setup cache database
    db = dbm.open('db_test', 'c')
    cache_enabled = True

    # Generate MD5 key
    input_bytes = name.encode("utf-8")
    input_md5 = hashlib.md5(input_bytes).hexdigest()

    print("MD5 key:")
    print(input_md5)

    from_cache = False

    # If db has value in cache
    if cache_enabled and input_md5 in db:
        output_bytes = db[input_md5]
        output = output_bytes.decode("utf-8")

        from_cache = True

    else:
        # Cache output in db
        output = "Hello, {}".format(name)

        output_bytes = output.encode("utf-8")
        db[input_md5] = output_bytes

        from_cache = False

    print("Output: '%s' Cached: %s" % (output, "True" if from_cache else "False"))
