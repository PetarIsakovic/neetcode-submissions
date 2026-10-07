class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for item in strs:
            array = [0] * 26
            for character in item:
                index = ord(character) - ord('a')
                array[index] = array[index]+1
            key = tuple(array)
            if key not in dic:
                dic[key] = [item]
            else:
                dic[key].append(item)
        
        output = []
        for item in dic.values():
            output.append(item)
        return output
                