class Solution(object):

    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        n = len(s)

        # Store first and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i in range(n):
            idx = ord(s[i]) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid substring for each character
        for c in range(26):

            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]

            i = left
            valid = True

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character appears before our left boundary
                if first[idx] < left:
                    valid = False
                    break

                # Include all occurrences of this character
                right = max(right, last[idx])

                i += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        # Greedily select non-overlapping intervals
        for left, right in intervals:

            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result