class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Dict = {}

        for c in s1:
            s1Dict[c] = 1 + s1Dict.get(c, 0)

        l = 0
        for r in range(len(s2)):
            s1Dict[s2[r]] = s1Dict.get(s2[r], 0) - 1
            while s1Dict[s2[r]] < 0:
                s1Dict[s2[l]] += 1
                l += 1
            if (r - l + 1 == len(s1)):
                return True
        
        return False

        