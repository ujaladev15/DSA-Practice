class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            # Opening bracket
            if char in "([{":
                stack.append(char)

            # Closing bracket
            else:
                # No opening bracket available
                if not stack:
                    return False

                # Check matching bracket
                if stack.pop() != pairs[char]:
                    return False

        # All opening brackets should be closed
        return len(stack) == 0