class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Count how many numbers contain each bit
        cnt = [0] * 31

        for x in nums:
            for b in range(31):
                if x & (1 << b):
                    cnt[b] += 1

        ans = 0

        # Build the largest possible number each time
        for _ in range(k):
            x = 0

            for b in range(31):
                if cnt[b] > 0:
                    x |= (1 << b)
                    cnt[b] -= 1

            ans = (ans + x * x) % MOD

        return ans