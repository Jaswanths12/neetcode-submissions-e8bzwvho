from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        
        # bucket[i] = list of numbers that appear i times
        bucket = [[] for _ in range(n + 1)]
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []
        # Start from highest frequency
        for freq in range(n, 0, -1):
            if bucket[freq]:
                result.extend(bucket[freq])
                if len(result) >= k:
                    return result[:k]
        
        return result