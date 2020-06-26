import time


def logFunc(func):
    def inner(*args):

        start = time.time()
        func(*args)
        end = time.time()
        print(end-start)
    return inner

@logFunc
def sort_():
    print("hello")

if __name__ == '__main__':
    sort_()
