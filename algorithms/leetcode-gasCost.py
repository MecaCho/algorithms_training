class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        def cycle_check(start):
            length = len(gas)
            gas_has = 0
            remian = 0
            seq = 0
            for i in range(length):
                seq = (start + i) % length
                if gas_has + gas[seq] < cost[seq]:
                    return False

                remain = gas[seq] - cost[seq]
                gas_has += remain
                # print(gas_has, seq, "seq;", gas_has + gas[seq], cost[seq])

            # if gas_has + gas[seq+1] - cost[seq+1] >= 0:
            return True

        asserts = []
        begins = []
        for i in range(len(gas)):
            remain = gas[i] - cost[i]
            asserts.append(remain)
            if remain >= 0:
                begins.append(i)
        for start in begins:
            # print(start)
            if cycle_check(start):
                return start
        return -1



if __name__ == '__main__':
    demo = Solution()
    # [4,5,2,6,5,3]
# [3,2,7,3,2,9]
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    # gas = [5, 1, 2, 3, 4]
    # cost = [4, 4, 1, 5, 1]

    gas =  [4,5,2, 6, 5, 3]
    cost = [3,2,7, 3, 2, 9]
    print(demo.canCompleteCircuit(gas, cost))
