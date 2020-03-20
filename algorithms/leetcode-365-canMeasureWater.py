class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        import math
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or (x+y) == z
        return z % math.gcd(x, y) == 0

if __name__ == '__main__':
    demo = Solution()
    print(demo.canMeasureWater(2,6, 5))
