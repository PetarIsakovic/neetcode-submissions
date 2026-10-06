class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False
        map1 = {}
        for item in s:
            if item not in map1:
                map1[item] = 1
            else:
                map1[item] += 1
        for item in t:
            if item not in map1:
                return False
            else:
                if map1[item] > 0:
                    map1[item] -= 1
                else:
                    return False
        return True