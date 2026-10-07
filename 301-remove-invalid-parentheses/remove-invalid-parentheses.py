class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = {s}
        result = []

        while queue:
            # Check current level
            for string in queue:
                if isValid(string):
                    result.append(string)

            # If valid strings found, this is minimum removal
            if result:
                return result

            # Generate next level by removing one parenthesis
            next_queue = set()

            for string in queue:
                for i in range(len(string)):
                    if string[i] in "()":
                        next_queue.add(string[:i] + string[i + 1:])

            queue = next_queue

        return result
        