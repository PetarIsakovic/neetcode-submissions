class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total = 0
        containsZero = False
        for item in nums:
            if item != 0 and total == 0:
                total = 1
            if item != 0:
                total *= item
            elif containsZero and item == 0:
                total = 0
                break
            else:
                containsZero = True
        for item in nums:
            if item != 0:
                if not containsZero:
                    output.append(int(total/item))
                else:
                    output.append(0)
            else:
                output.append(int(total))

        return output

            