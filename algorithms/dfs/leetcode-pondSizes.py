# encoding=utf8

'''
面试题 16.19. Pond Sizes LCCI
You have an integer matrix representing a plot of land, where the value at that loca­tion represents the height above sea level. A value of zero indicates water. A pond is a region of water connected vertically, horizontally, or diagonally. The size of the pond is the total number of connected water cells. Write a method to compute the sizes of all ponds in the matrix.

Example:

Input: 
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
Output:  [1,2,4]
Note:

0 < len(land) <= 1000
0 < len(land[i]) <= 1000
'''
