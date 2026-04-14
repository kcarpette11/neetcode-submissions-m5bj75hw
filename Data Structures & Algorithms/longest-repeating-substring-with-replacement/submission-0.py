class Solution:
   def characterReplacement(self, s: str, k: int) -> int:
    # use sliding window method
    max_length = 0
    left = 0
    right = 0
    max_freq = 0
    letters = {}

    while right < len(s):
        current_char = s[right]
        letters[current_char] = letters.get(current_char, 0) + 1

        # update max frequency
        max_freq = max(max_freq, letters[current_char])

        # check if the window size is valid
        if (right - left + 1) - max_freq > k:
            left_char = s[left]
            letters[left_char] -= 1
            left += 1
        
        # update max_length
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length