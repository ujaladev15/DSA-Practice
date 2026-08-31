class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        # Put each number in its correct position
        i = 0

        while i < n:
            correct_index = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # Find the first number that is not in its correct position
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1