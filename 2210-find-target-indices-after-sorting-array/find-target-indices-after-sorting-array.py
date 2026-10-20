class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        count = 0

        for num in nums:
            if num < target:
                start += 1
            elif num == target:
                count += 1

        return list(range(start, start + count))