class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        n = len(nums)

        # Segment tree:
        #
        # prod[node] = product of the whole segment % k
        #
        # pref[node][r] = number of non-empty prefixes of this
        # segment whose product % k == r
        #
        # Since k <= 5, store everything in flat arrays.

        size = 4 * n + 5

        prod = [0] * size

        # pref[node * k + r]
        pref = [0] * (size * k)

        def build(node, l, r):
            if l == r:
                p = node * k
                rem = nums[l] % k

                prod[node] = rem
                pref[p + rem] = 1
                return

            mid = (l + r) >> 1
            left = node << 1
            right = left | 1

            build(left, l, mid)
            build(right, mid + 1, r)

            prod[node] = (prod[left] * prod[right]) % k

            p = node * k
            lp = left * k
            rp = right * k

            # Prefixes completely inside left.
            for x in range(k):
                pref[p + x] = pref[lp + x]

            # Prefix = whole left + prefix of right.
            pl = prod[left]

            for x in range(k):
                cnt = pref[rp + x]
                if cnt:
                    pref[p + (pl * x) % k] += cnt

        def update(node, l, r, idx, value):
            if l == r:
                rem = value % k

                prod[node] = rem

                p = node * k

                # Clear old prefix counts.
                for x in range(k):
                    pref[p + x] = 0

                pref[p + rem] = 1
                return

            mid = (l + r) >> 1
            left = node << 1
            right = left | 1

            if idx <= mid:
                update(left, l, mid, idx, value)
            else:
                update(right, mid + 1, r, idx, value)

            prod[node] = (prod[left] * prod[right]) % k

            p = node * k
            lp = left * k
            rp = right * k

            # Rebuild prefix distribution.
            for x in range(k):
                pref[p + x] = pref[lp + x]

            pl = prod[left]

            for x in range(k):
                cnt = pref[rp + x]
                if cnt:
                    pref[p + (pl * x) % k] += cnt

        # Query only needs to return:
        #
        # product of queried range
        # prefix distribution of queried range
        #
        # Instead of allocating lists, return a tuple containing
        # the product and a small tuple of k counts.

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                p = node * k
                return (
                    prod[node],
                    tuple(pref[p + x] for x in range(k))
                )

            mid = (l + r) >> 1
            left = node << 1
            right = left | 1

            if qr <= mid:
                return query(left, l, mid, ql, qr)

            if ql > mid:
                return query(right, mid + 1, r, ql, qr)

            lp, lpref = query(left, l, mid, ql, qr)
            rp, rpref = query(right, mid + 1, r, ql, qr)

            result = list(lpref)

            # Entire left + prefix of right.
            for x in range(k):
                cnt = rpref[x]
                if cnt:
                    result[(lp * x) % k] += cnt

            return (
                (lp * rp) % k,
                tuple(result)
            )

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Persistent update.
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # We only need prefix counts.
            _, p = query(1, 0, n - 1, start, n - 1)

            ans.append(p[x])

        return ans