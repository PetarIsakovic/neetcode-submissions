import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        dic = {}
        for item in nums:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        
        array = []
        for key, value in dic.items():
            array.append((value, key))
        
        heapq.heapify_max(array)

        output = []
        for num in range(k):
            output.append(heapq.heappop_max(array)[1])

        return output
        