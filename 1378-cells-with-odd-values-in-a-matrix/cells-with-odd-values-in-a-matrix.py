class Solution:
    def oddCells(self, m: int, n: int, indices):
        rows = [0] * m
        cols = [0] * n

        # Count row and column increments
        for r, c in indices:
            rows[r] ^= 1   # Toggle parity
            cols[c] ^= 1

        odd = 0

        # Count cells with odd values
        for i in range(m):
            for j in range(n):
                if rows[i] ^ cols[j]:
                    odd += 1

        return odd
        