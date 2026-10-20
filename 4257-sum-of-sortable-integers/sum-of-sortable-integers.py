class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            possible = True
            prev_max = None

            for start in range(0, n, k):
                end = start + k

                # Find min and max of this block
                mn = nums[start]
                mx = nums[start]

                # Count descents inside the block
                descents = 0

                for i in range(start + 1, end):
                    mn = min(mn, nums[i])
                    mx = max(mx, nums[i])

                    if nums[i - 1] > nums[i]:
                        descents += 1

                # Circular descent
                if nums[end - 1] > nums[start]:
                    descents += 1

                # Block must be sortable by rotation
                if descents > 1:
                    possible = False
                    break

                # Blocks must appear in global sorted order
                if prev_max is not None and prev_max > mn:
                    possible = False
                    break

                prev_max = mx

            if possible:
                ans += k

        return ans