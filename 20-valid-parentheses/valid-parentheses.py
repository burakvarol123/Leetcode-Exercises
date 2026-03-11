class Solution:
    def isValid(self, s: str) -> bool:
        valid ={"(": ")", "{" : "}", "[": "]"}
        seen = []
        for char in s:
            if char in valid:
                seen.append(char)
            else:
                if not seen:
                    return False
                if valid[seen[-1]] == char:
                    seen.pop()
                else:
                    return False
        return not seen
                
        
            