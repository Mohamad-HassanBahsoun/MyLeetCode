from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        duplicate = defaultdict(int)

        for i in nums:
            duplicate[i] +=1
            if(duplicate[i] >1):
                return True
        return False