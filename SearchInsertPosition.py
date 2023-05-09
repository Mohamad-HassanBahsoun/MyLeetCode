class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if(i >=target):
                x = nums.index(i)
                return x
        return len(nums)