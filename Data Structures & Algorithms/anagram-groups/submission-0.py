class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            # Key = sorted version of the word
            key = ''.join(sorted(word))
            
            # Add word to its group
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        # Return all groups
        return list(groups.values())