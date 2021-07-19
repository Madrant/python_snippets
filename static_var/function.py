#!/usr/bin/python3


def func():
    if not hasattr(func, "counter"):
        func.counter = 0

    if hasattr(func, "counter"):
        print("Counter: %u" % (func.counter))
        func.counter += 1

if __name__ == "__main__":
    func()
    func()
    func()
