def see():
    heights = [1, 2, 3, 2, 4, 5, 7, 4, 2, 1]
    n = len(heights)
    res = [0]*n
    stack = []
    for i in range(n-1, -1, -1):
        h = heights[i]
        while stack and h > stack[-1]:
            stack.pop()
            res[i] += 1
        if stack:
            res[i] += 1
        stack.append(h)
    return res

if __name__ == "__main__":
    res = see()
    print(res)

