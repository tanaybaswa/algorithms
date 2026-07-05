from _heapq import heappop
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        
        count = Counter(nums)
        heap = []

        for num, freq in count.items():

            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        output = [x[1] for x in heap]

        return output
        