class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_num(num):
            res = 0
            while num:
                res += (num % 10) ** 2
                num = int(num / 10)
            return res

        num_list = [n]
        while n != 1:
            n = get_num(n)
            print(n)
            if n in num_list:
                return False
            num_list.append(n)
        return True


if __name__ == '__main__':
    demo = Solution()
    print(demo.isHappy(19))