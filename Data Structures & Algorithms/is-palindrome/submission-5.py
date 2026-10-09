class Solution:
    def isPalindrome(self, s: str) -> bool:
        # [1] Initilize two pointers at both ends
        l, r = 0, len(s) - 1


        while l < r:
            
            # [3] Skip non-alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            # [4] Compare characters case-insensitively
            if s[l].lower() != s[r].lower():
                return False

            # [2] Move pointers inward
            l, r = l + 1 , r - 1
        return True
            
