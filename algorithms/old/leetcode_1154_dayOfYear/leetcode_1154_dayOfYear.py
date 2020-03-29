class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        import time
        time_ = time.strptime(date, "%Y-%m-%d")
        print time_.tm_yday
        print time.strptime(str(date), "%Y-%m-%d").tm_yday
        return time_

if __name__ == '__main__':
    demo = Solution()
    demo.dayOfYear("2019-08-10")
