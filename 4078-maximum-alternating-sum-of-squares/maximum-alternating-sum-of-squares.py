class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=lambda x: abs(x))

        ans = 0
        n = len(nums)

        for i, x in enumerate(nums):
            if i >= n // 2:
                ans += x * x
            else:
                ans -= x * x

        return ans