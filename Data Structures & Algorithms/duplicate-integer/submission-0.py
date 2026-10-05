class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # how make a hashmap, how do for loop in python
        map = {}

        for item in nums:
            if item not in map:
                map[item] = 1
            else:
                return True
        return False