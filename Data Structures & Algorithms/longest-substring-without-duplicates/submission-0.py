class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0 
        res = 0 
        char_set = set()

        while r < n:
            if s[r] not in char_set:
                char_set.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else: 
                char_set.remove(s[l])
                l += 1



        return res
        