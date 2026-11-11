class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (sorted(s) == sorted(t) and set(s) == set(t))