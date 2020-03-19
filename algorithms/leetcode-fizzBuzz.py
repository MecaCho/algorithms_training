class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def getnum(num):

            if num % 5 == 0 and num % 3 == 0:
                return "FizzBuzz"
            elif num % 3 == 0:
                return "Fizz"
            else:
                return str(num)

        return [getnum(i) for i in range(1, n + 1)]

if __name__ == '__main__':
    demo = Solution()
    print(demo.fizzBuzz(15))

