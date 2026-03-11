class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for string in strs:
            if len(string) < len(shortest):
                shortest = string
        for string in strs:
            for k in range(len(shortest)):
                last = len(shortest) - k 
                if string.startswith(shortest):
                    continue
                shortest = shortest[:-1]
        return shortest 
            



        
         

        
