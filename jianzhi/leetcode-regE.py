import re


if __name__ == '__main__':
    s = "123e10"
    import string
    print(s.isnumeric())
    res = re.match(r' *[+-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)(e[+-]?[0-9]+)? *$', s)
    print(res)