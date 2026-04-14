class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        # converting digits to char 
        if not digits:
            return []
        DigitsToChar = { "2": "abc", "3":"def", "4": "ghi", "5":"jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        def backtrack(i,currStr):
            if len(currStr) == len(digits): # if the length of the two strings match
                res.append(currStr) # add string to result 
                return
            for char  in DigitsToChar[digits[i]]:
                backtrack(i + 1, currStr + char)


        backtrack(0,"")
        return res
        