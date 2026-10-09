class Solution:

    def encode(self, strs: List[str]) -> str:
        # word tomato potato
        # 123,3,21,1443|1,2,3,4,5|6,3,2,5,6|*|
        output = ""
        for word in strs:
            if(len(word) == 0):
                output += "*|"
                continue
            for index, character in enumerate(word):
                value = ord(character)
                output += str(value)
                if(index != len(word)-1):
                    output += ","
            output += "|"
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        words = s.split("|")
        for i in range(0, len(words)-1):
            if(words[i] == "*"):
                output.append("")
                continue
            word = ""
            for character in words[i].split(","):
                word += chr(int(character))
            output.append(word)
        return output