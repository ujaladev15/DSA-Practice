class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1       # '*' acts as ')'
                high += 1      # '*' acts as '('

            low = max(low, 0)

            if high < 0:
                return False

        return low == 0