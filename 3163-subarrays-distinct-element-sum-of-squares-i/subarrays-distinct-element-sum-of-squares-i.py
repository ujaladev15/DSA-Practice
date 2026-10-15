class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for i in range(len(nums)):
            s = set()

            for j in range(i, len(nums)):
                s.add(nums[j])
                distinct = len(s)
                ans += distinct * distinct

        return ans