#!/usr/bin/python3

import concurrent.futures

def process_input(name):
    print("Hello, %s" % (name))

    return name

if __name__ == "__main__":
    params = ["John", "Ben", "Jesus"]
    print(params)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_input, param) for param in params]
        print(futures)

    for future in futures:
        name = future.result()
        print(name)

    # Alternate usage in case of a process deadlock using 'with'
    pool = concurrent.futures.ProcessPoolExecutor()
    futures = []

    for param in params:
        future = pool.submit(process_input, param)
        futures.append(future)

    for future in futures:
        name = future.result()
        print(name)
