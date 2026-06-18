# encoding=utf8

'''
1344. Angle Between Hands of a Clock

Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

 

Example 1:

Input: hour = 12, minutes = 30
Output: 165

Example 2:

Input: hour = 3, minutes = 30
Output: 75

Example 3:

Input: hour = 3, minutes = 15
Output: 7.5

 

Constraints:

    1 <= hour <= 12
    0 <= minutes <= 59
'''

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 计算分针角度：每分钟走 6 度
        minute_angle = minutes * 6
        
        # 计算时针角度：每小时走 30 度，每分钟额外走 0.5 度
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        # 计算两针之间的角度差
        diff = abs(hour_angle - minute_angle)
        
        # 返回较小的夹角
        return min(diff, 360 - diff)     
           
