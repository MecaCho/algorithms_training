class Solution:
        def minStoneSum(self, piles: List[int], k: int) -> int:
                    h = [-a for a in piles]
                            heapify(h)
                                    for i in range(k):
                                                    a = -heappop(h)
                                                                a = a - a//2
                                                                            heappush(h, -a)
                                                                                    return -sum(h)

