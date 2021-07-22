#!/usr/bin/python3

import concurrent.futures

def process_input(name):
    print("Hello, %s" % (name))

    return name

if __name__ == "__main__":
    names = ["John", "Ben", "Jesus"]
    print(names)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_input, name) for name in names]
        print(futures)

    for future in futures:
        name = future.result()
        print(name)
