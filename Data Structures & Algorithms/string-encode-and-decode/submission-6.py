class Solution:
    #brute force approach
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "emptylist"

        string = ""
        for i in range(len(strs)):
            if i == len(strs)-1:
                string += f"{strs[i]}"
            else:
                string += f"{strs[i]}delim"

        return string


    def decode(self, s: str) -> List[str]:
        if s is "emptylist":
            return []
        return s.split("delim")