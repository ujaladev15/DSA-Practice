class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # We need to calculate comb(n + k - 1, 2*k) % MOD
        # Using a direct multiplicative formula to compute combination
        numerator = 1
        denominator = 1
        
        # Choose the smaller of the two terms for efficiency
        total_elements = n + k - 1
        choose_elements = 2 * k
        
        if choose_elements > total_elements:
            return 0
            
        for i in range(choose_elements):
            numerator = (numerator * (total_elements - i)) % MOD
            denominator = (denominator * (i + 1)) % MOD
            
        # Modular inverse using Fermat's Little Theorem
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD