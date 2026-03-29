class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find min length string (to avoid index out of range)
        min_len = min(len(s) for s in strs)
        
        # Compare character by character
        for i in range(min_len):
            char = strs[0][i]              # take char from first string
            for s in strs[1:]:
                if s[i] != char:
                    return strs[0][:i]     # return prefix up to this position
        
        # If all strings matched up to min length
        return strs[0][:min_len]