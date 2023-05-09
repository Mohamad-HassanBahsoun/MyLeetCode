class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        popping = []
        index = 0
        for i in range(0,len(nums)-1):
            if(nums[i] != nums[i+1]):
                nums[index] = nums[i]
                index+=1     
        nums[index] = nums[len(nums)-1]
        index+=1

        return index