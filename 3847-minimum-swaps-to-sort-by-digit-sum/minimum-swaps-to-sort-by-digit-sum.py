class Solution:
    def minSwaps(self, nums):
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)

        # Target sorted order
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Where each value should go
        pos = {value: i for i, value in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps