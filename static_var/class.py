#!/usr/bin/python3

class Test():

    def func(self):
        if not hasattr(self, "counter"):
            self.counter = 0

        if hasattr(self, "counter"):
            print("Counter: %u" % (self.counter))
            self.counter += 1

if __name__ == "__main__":
    test1 = Test()
    test2 = Test()

    test1.func()
    test1.func()
    test1.func()

    test2.func()
    test2.func()
