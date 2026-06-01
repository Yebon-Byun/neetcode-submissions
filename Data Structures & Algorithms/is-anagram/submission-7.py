class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # set으로는 부족 -> 같은 알파벳들이 여러 개 나올 수 있음