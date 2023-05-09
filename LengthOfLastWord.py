class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = s.split(" ")
        for i in range(len(list1)-1,-1,-1):
            if(list1[i]):
                return len(list1[i])