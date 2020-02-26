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

