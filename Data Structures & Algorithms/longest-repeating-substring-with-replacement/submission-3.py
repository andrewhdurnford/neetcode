class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = l = maxf = 0

        for r, n in enumerate(s):
            count[n] += 1
            maxf = max(maxf, count[n])

            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res