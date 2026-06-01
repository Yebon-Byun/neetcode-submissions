class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        map_char = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        } 
        
        def backtrack(i, comb_char):
            if len(digits) == len(comb_char):
                res.append(comb_char)
                return

            for c in map_char[digits[i]]:
                backtrack(i + 1, comb_char + c)
        
        if digits:
            backtrack(0, "")

        return res


