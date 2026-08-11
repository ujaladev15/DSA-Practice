class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maximum = 0

        for num in nums:
            if num == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                count = 0

        return maximum