class Solution(object):

    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """

        total = 0
        start = 1000
        commas = 1

        while start <= n:
            end = start * 1000 - 1

            count = min(n, end) - start + 1

            total += count * commas

            start *= 1000
            commas += 1

        return total