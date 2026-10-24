class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count the occurrence of each character
        count = {}
        # longest substring we can create with k replacements
        res = 0

        l = 0
        for r in range(len(s)):
            # update the frequency of char at right pointer
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l +  1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # r - l + 1 is the length of the window
            res = max(res, r - l + 1)

        return res