class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        memo = {}

        def dp(i, j):

            # If already calculated
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern finished
            if j == len(p):
                return i == len(s)

            # Check current character match
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == ".")
            )

            # Check if next character is *
            if j + 1 < len(p) and p[j + 1] == "*":

                # Option 1: Skip x*
                # Option 2: Use x and continue
                answer = (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )

            else:
                answer = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = answer

            return answer

        return dp(0, 0)