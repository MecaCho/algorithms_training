


class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        for i in range(2**k):
            print(bin(i)[2:].ljust(k, "0"))
            ch = bin(i)[2:].ljust(k, "0")
            if ch not in s:
                return False
        return True


class Solution1(object):

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max_sum = 0

        def choice(deep, pre_l, pre_r, sum_l, sum_r):
            if deep == len(grid):
                self.max_sum = max(sum_l + sum_r, self.max_sum)
            else:
                for i, j in [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 0), (0, 1), (1, 0), (1, -1), (1, 1)]:
                    new_ch_l = pre_l + i

                    new_ch_r = pre_r + j

                    if 0 <= new_ch_l < len(grid[0]) and 0 <= new_ch_r < len(grid[0]):
                        new_res_l = sum_l + grid[deep][new_ch_l]
                        new_res_r = sum_r + grid[deep][new_ch_r]
                        if new_ch_l == new_ch_r:
                            new_res_l -= sum_r + grid[deep][new_ch_r]
                        choice(deep + 1, new_ch_l, new_ch_r, new_res_l, new_res_r)

        r = len(grid[0]) - 1
        choice(1, 0, r, grid[0][0], grid[0][r])
        return self.max_sum


class Solution12(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #         self.max_sum = 0
        #         def choice(deep, pre_l,pre_r, sum_all):
        #             if deep == len(grid):
        #                 self.max_sum = max(sum_all, self.max_sum)
        #             else:
        #                 for i, j in [(-1, 0),(-1, -1), (-1, 1),(0, -1), (0,0), (0,1), (1, 0), (1, -1), (1, 1)]:
        #                     new_ch_l = pre_l + i

        #                     new_ch_r = pre_r + j

        #                     if 0 <= new_ch_l < len(grid[0]) and 0 <= new_ch_r < len(grid[0]):
        #                         new_sum_all = sum_all + grid[deep][new_ch_l]+grid[deep][new_ch_r]

        #                         if new_ch_l == new_ch_r:
        #                             new_sum_all -= grid[deep][new_ch_r]
        #                         choice(deep+1, new_ch_l, new_ch_r, new_sum_all)

        #         r = len(grid[0]) - 1
        #         choice(1, 0, r, grid[0][0]+grid[0][r])
        #         return self.max_sum

        dp = [[[grid[i][j], 0] for j in range(len(grid[0]))] for i in range(len(grid))]
        print(dp)


class Solution2(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts += [0, h]
        horizontalCuts = sorted(horizontalCuts)
        h_s = [horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts))]
        max_h = max(h_s)

        verticalCuts += [0, w]
        verticalCuts = sorted(verticalCuts)
        v_s = [verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts))]

        # print(h_s, v_s)

        max_v = max(v_s)

        return (max_h * max_v) % (10 ** 9 + 7)


if __name__ == '__main__':
    demo = Solution()
    res = demo.hasAllCodes("0110", 2)