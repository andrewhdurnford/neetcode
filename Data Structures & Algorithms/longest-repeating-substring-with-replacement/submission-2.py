class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        count = defaultdict(int)
        l = 0
        common = 0

        for r, c in enumerate(s):
            count[c] = count[c] + 1
            common = max(common, count[c])

            while(r - l + 1) - common > k:
                count[s[l]] -= 1
                l += 1

            maxi = max(maxi, r - l + 1)

        return maxi