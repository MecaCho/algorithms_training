# encoding=utf8

'''

「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。 给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。

示例 1：

输入：cards = [1,2,8,9], cnt = 3

输出：18

解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。

示例 2：

输入：cards = [3,3,1], cnt = 1

输出：0

解释：不存在获取有效得分的卡牌方案。

提示：

1 <= cnt <= cards.length <= 10^5
1 <= cards[i] <= 1000
'''

class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        res = 0
        min_0 = None
        min_1 = None
        while cnt:
            min_num = cards.pop()
            if min_num & 1:
                min_1 = min_num
            else:
                min_0 = min_num    
            res += min_num
            cnt -= 1
            
        if res % 2 == 0:
            return res
        max0 = None
        max1 = None   
        
        while cards:
               max_num = cards.pop()
               if max0 is None:
                   if max_num % 2 == 0:
                       max0  = max_num
               if max1 is None:  
                   if max_num % 2 == 1:
                       max1  = max_num
               if max1 and max0:
                   break     
        #print(min_1,min_0,max0,max1)              
        if max1 and max0 and min_1 and min_0:
            return res -min(min_1-max0,min_0-max1)
        if max1 and min_0:
            return res - (min_0-max1)
        if max0 and min_1:
            return res - (min_1-max0)    
        return 0              
                
