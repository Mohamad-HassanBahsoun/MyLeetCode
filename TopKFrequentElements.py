from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        c = Counter(nums)

        res = []

        for i in range(0,k):
            keyV=max(c,key=c.get)
            res.append(keyV)
            c[max(c,key=c.get)] = 0
        return res