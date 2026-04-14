class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # for grouping items
        max_char_count = 26 # max amount of characters is 26, 26 letters in alphabet
        for s in strs: 
            #setup frequency count
            freq_count = [0] * max_char_count
            for c in s:
                freq_count[ord(c)-ord('a')] += 1
            res[tuple(freq_count)].append(s)
        return list(res.values())
           


   

        