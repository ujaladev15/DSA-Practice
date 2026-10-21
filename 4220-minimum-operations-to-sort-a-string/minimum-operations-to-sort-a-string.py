class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # With 2 characters, the only possible substring is
        # the entire string, which is not allowed.
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Minimum character is already at the beginning
        # OR maximum character is already at the end.
        # Sort the remaining proper substring.
        if s[0] == mn or s[-1] == mx:
            return 1

        # If min or max occurs somewhere in the middle,
        # we can move it to its correct side in one operation,
        # then sort the remaining part.
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # min is only at the end and max is only at the beginning.
        # Need 3 operations.
        return 3