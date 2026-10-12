class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_bracket = {")" : "(" , "]" : "[" , "}" : "{"}
        
        for c in s:
            if c in close_bracket:
                if stack and stack[-1] == close_bracket[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        
        return not stack