class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, item in enumerate(nums):
            if item not in map:
                map[item] = index
        for index, item in enumerate(nums):
            holder = target-item
            if holder in map and index != map[holder]:
                if(map[holder] < index):
                    return [map[holder], index]
                else:
                    return [index, map[holder]]