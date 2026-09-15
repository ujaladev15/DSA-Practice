class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)

        # pal[l][r] = whether s[l:r+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table by increasing length
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r]:
                    if length <= 2:
                        pal[l][r] = True
                    else:
                        pal[l][r] = pal[l + 1][r - 1]

        # dp[i] = maximum number using s[0:i]
        dp = [0] * (n + 1)

        for r in range(n):
            # Don't use a substring ending at r
            dp[r + 1] = dp[r]

            # Try every palindrome ending at r
            for l in range(r + 1):
                if r - l + 1 >= k and pal[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n]