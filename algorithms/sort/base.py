import time


def logFunc(func):
    def inner(*args):

        start = time.time()
        func(*args)
        end = time.time()
        msg = "{:<20s} with {} nums,cost time: {}".format(func.__name__, len(*args),  end-start)
        print(msg)
    return inner
