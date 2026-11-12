class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0

            counts[num] += 1

        result = []

        for i in range(k):
            max_num = max(counts, key=counts.get)
            result.append(max_num)
            del counts[max_num]
        
        return result