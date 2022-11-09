class Solution:
    def findMaxForm(self, trs: List[str], m: int, n: int) -> int:
        counts = [None] * len(trs)
        for idx, s in enumerate(trs):

            zeros, ones = 0, 0

            for char in s:
                if char == '0':
                    zeros += 1
                else:
                    ones += 1

            counts[idx] = (zeros, ones)

        tot = len(trs)


        @lru_cache(None)
        def solve(idx, zeros_count, ones_count):

            if idx >= tot:
                return float('-inf') if zeros_count > m and ones_count > n else 0

            # include in subset
            inc = 0
            zero, one = counts[idx]
            if (zeros_count + zero) <= m and (one + ones_count) <= n:
                inc = 1 + solve(idx+1, zeros_count + zero, one + ones_count)

            # not include
            not_inc = solve(idx+1, zeros_count, ones_count)

            return max(inc, not_inc)


        return solve(0, 0, 0)