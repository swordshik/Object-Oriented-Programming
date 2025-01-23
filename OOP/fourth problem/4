class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tt = t
        for i in range(len(s)):
            tt = tt.replace(s[i], '', 1)
        return (True and ((tt == '') and (len(s)==len(t))))