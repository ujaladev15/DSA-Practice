class Solution:
    def totalNumbers(self, digits):
        count = 0

        # Frequency of each digit
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        # Try every 3-digit even number
        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Check whether we have enough copies of each digit
            if a == b == c:
                if freq[a] >= 3:
                    count += 1

            elif a == b:
                if freq[a] >= 2 and freq[c] >= 1:
                    count += 1

            elif a == c:
                if freq[a] >= 2 and freq[b] >= 1:
                    count += 1

            elif b == c:
                if freq[b] >= 2 and freq[a] >= 1:
                    count += 1

            else:
                if freq[a] >= 1 and freq[b] >= 1 and freq[c] >= 1:
                    count += 1

        return count