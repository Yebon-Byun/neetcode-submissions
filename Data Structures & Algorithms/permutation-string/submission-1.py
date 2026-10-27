class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A matching window must be exactly as long as s1.
        if len(s1) > len(s2): 
            return False

        # Count characters in s1 and the first k characters of s2.
        target = [0] * 26
        window = [0] * 26
        for i in range(len(s1)):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        # Slide a fixed-size window: add right, remove left.
        for right in range(len(s1), len(s2)):
            if window == target:
                return True

            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[right - len(s1)]) - ord('a')] -= 1

        # Check the final window, which is not tested in the loop.
        return window == target

