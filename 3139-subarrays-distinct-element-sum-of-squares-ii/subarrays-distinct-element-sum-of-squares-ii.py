class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        sm = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, length, k):
            # d -> d + k
            sq[node] = (
                sq[node]
                + 2 * k * sm[node]
                + k * k * length
            ) % MOD

            sm[node] = (
                sm[node] + k * length
            ) % MOD

            lazy[node] += k

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            k = lazy[node]

            apply(node * 2, mid - l + 1, k)
            apply(node * 2 + 1, r - mid, k)

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, r - l + 1, 1)
                return

            push(node, l, r)

            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            sm[node] = (
                sm[node * 2] + sm[node * 2 + 1]
            ) % MOD

            sq[node] = (
                sq[node * 2] + sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            prev = last.get(x, -1)

            # These starting positions get one new distinct value.
            update(1, 0, n - 1, prev + 1, r)

            # Sum of squares of all subarrays ending at r.
            ans = (ans + sq[1]) % MOD

            last[x] = r

        return ans