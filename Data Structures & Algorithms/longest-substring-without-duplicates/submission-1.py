class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        count = Counter()

        l = 0
        r = 0
        n = len(s)

        output = 0

        while r < n:

            if s[r] in count and count[s[r]] > 0:
                while l <= r and count[s[r]] > 0:
                    count[s[l]] -= 1
                    l += 1

            output = max(output, r - l + 1)

            count[s[r]] += 1
            r += 1

        return output
        