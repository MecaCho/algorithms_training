
def qrt(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n
    l, r = 1, n - 1
    count = 0
    while l <= r:
        count += 1
        mid = float((l+r)/2)
        abs_ = abs(float(mid * mid - n))
        print l, r, abs_
        if abs_ < 0.0001:
            return mid
        elif mid * mid > n:
            r = mid
        elif mid * mid < n:
            l = mid
    print "count :{}".format(count)


if __name__ == '__main__':
    print qrt(100)
    # print qrt(98)

