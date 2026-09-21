class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with nums[i]
            rem = num % k
            new_dp[rem] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r]:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]

            # All subarrays ending here contribute to the answer
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result
        