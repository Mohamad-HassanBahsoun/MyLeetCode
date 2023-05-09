class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}
        for key, value in enumerate(nums):
            diff = target - value
            if(diff in prevMap):
                return [prevMap[diff], key]
            prevMap[value] = key

        return