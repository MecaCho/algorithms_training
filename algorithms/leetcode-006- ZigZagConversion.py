class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        index = 0
        length = len(s)
        ret = ""
        if length < 3 or numRows ==1 or length <= numRows:
            return s
        numcCol = length / (numRows*2 -2) + 1
        numCols = (numRows-1) * numcCol + 1
        aList = [[" " for i in range(numCols)] for j in range(numRows)]
        for i in range(numCols):
            for j in range(numRows):
                if (i % (numRows-1))==0 or (i + j)%(numRows -1)==0:
                    if index < length and aList[j][i] == " ":
                        aList[j][i] = s[index]
                        index += 1

        # print(aList)
        for i in range(numRows):
            for j in range(numCols):
                if aList[i][j] != " ":
                    ret += aList[i][j] 
        return ret
   
'''
Note also that the copies are shallow; nested structures are not copied. This often haunts new Python programmers; consider:

>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]
What has happened is that [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are (pointers to) this single empty list. Modifying any of the elements of lists modifies this single list. You can create a list of different lists this way:

>>>
>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
'''

