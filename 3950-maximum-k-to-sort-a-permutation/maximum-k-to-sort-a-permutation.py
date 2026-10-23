class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Already sorted
        ans = -1

        for i in range(n):
            if nums[i] != i:
                if ans == -1:
                    ans = nums[i]
                else:
                    ans &= nums[i]

        # No misplaced elements
        if ans == -1:
            return 0

        return ans