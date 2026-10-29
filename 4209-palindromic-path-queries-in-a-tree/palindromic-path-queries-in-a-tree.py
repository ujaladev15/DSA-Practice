class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """

        # ---------- Tree ----------
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # ---------- HLD preprocessing ----------
        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # Iterative DFS
        order = [0]
        parent[0] = -1

        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        # Subtree sizes + heavy child
        for u in reversed(order):
            max_size = 0

            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]

                    if size[v] > max_size:
                        max_size = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        cur = 0

        # HLD decomposition
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1

                # Start light children later
                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # ---------- Fenwick Tree ----------
        bit = [0] * (n + 1)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            # XOR [0, i)
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def range_xor(l, r):
            # XOR [l, r)
            return prefix(r) ^ prefix(l)

        # Character -> bit mask
        masks = [1 << (ord(c) - ord('a')) for c in s]

        # Build Fenwick tree
        for i in range(n):
            add(pos[i], masks[i])

        # ---------- Path XOR using HLD ----------
        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:

                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                h = head[u]

                result ^= range_xor(pos[h], pos[u] + 1)

                u = parent[h]

            # Same chain
            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v] + 1)

            return result

        # ---------- Process queries ----------
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_mask = 1 << (ord(c) - ord('a'))

                # Remove old character
                add(pos[u], masks[u])

                # Add new character
                add(pos[u], new_mask)

                masks[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)

                # At most one bit can be set
                # for the string to be rearrangeable into a palindrome.
                answer.append((mask & (mask - 1)) == 0)

        return answer