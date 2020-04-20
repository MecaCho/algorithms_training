




if __name__ == '__main__':
    def check(pushed, poped):
        stack = []
        k = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            # print(stack)
            while stack and poped[k] == stack[-1]:
                stack.pop()
                k += 1
        print(stack, k)
    check([1,2,3,4,5], [4,5,2,3,1])