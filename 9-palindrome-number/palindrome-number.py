class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if x != 0 and x % 10 == 0:
            return False

        reversed_num = 0

        while x > reversed_num:
            digit = x % 10
            x = x // 10
            reversed_num = reversed_num * 10 + digit

        return x == reversed_num or x == reversed_num // 10