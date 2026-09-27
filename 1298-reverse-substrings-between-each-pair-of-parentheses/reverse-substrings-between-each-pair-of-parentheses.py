class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr = []

        for ch in s:
            if ch == '(':
                stack.append(curr)
                curr = []

            elif ch == ')':
                curr.reverse()
                prev = stack.pop()
                prev.extend(curr)
                curr = prev

            else:
                curr.append(ch)

        return ''.join(curr)
        