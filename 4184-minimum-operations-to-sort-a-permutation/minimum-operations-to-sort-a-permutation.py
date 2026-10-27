# class Solution(object):
#     def minOperations(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         ans = 10**9

#         # 1. Rotate Left k times
#         pos = nums.index(0)

#         ok = True
#         for i in range(n):
#             if nums[(pos + i) % n] != i:
#                 ok = False
#                 break

#         if ok:
#             ans = min(ans, pos)

#         # 2. Reverse, then Rotate Left k times
#         # Reversed array has 0 at n - 1 - pos
#         rpos = n - 1 - pos

#         ok = True
#         for i in range(n):
#             # index in original corresponding to index (rpos + i)
#             # in reversed array
#             idx = (n - 1 - (rpos + i)) % n

#             if nums[idx] != i:
#                 ok = False
#                 break

#         if ok:
#             ans = min(ans, 1 + rpos)

#         # 3. Rotate Left k times, then Reverse
#         # Before reversing, array must be [n-1, n-2, ..., 0]
#         pos = nums.index(n - 1)

#         ok = True
#         for i in range(n):
#             if nums[(pos + i) % n] != n - 1 - i:
#                 ok = False
#                 break

#         if ok:
#             ans = min(ans, pos + 1)

#         return -1 if ans == 10**9 else ans




class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Already sorted
        if nums == list(range(n)):
            return 0

        INF = 10**9
        ans = INF

        # -------------------------------------------------
        # 1. Only Left Rotations
        # -------------------------------------------------
        pos = nums.index(0)

        ok = True
        for i in range(n):
            if nums[(pos + i) % n] != i:
                ok = False
                break

        if ok:
            # Left rotate pos times
            ans = min(ans, pos)

            # Right rotate n-pos times = Reverse + Left + Reverse
            if pos != 0:
                ans = min(ans, n - pos + 2)

        # -------------------------------------------------
        # 2. Reverse + Left Rotations
        # -------------------------------------------------
        rpos = n - 1 - pos

        ok = True
        for i in range(n):
            idx = (n - 1 - (rpos + i)) % n

            if nums[idx] != i:
                ok = False
                break

        if ok:
            # Reverse + Left rpos
            ans = min(ans, 1 + rpos)

            # Equivalent Reverse + Left (n-rpos)
            ans = min(ans, 1 + (n - rpos))

        return -1 if ans == INF else ans