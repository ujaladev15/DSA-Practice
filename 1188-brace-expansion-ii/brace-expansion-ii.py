class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
                    # Union
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    # Parse everything inside {}
                    inside, i = parse(i + 1)

                    # Concatenation
                    current = {
                        a + b
                        for a in current
                        for b in inside
                    }

                else:
                    # Lowercase letter
                    current = {
                        word + expression[i]
                        for word in current
                    }
                    i += 1

            # Add the last part
            result |= current

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)