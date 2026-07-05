import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        buckets = [[] for i in range(n + 1)]
        count = Counter(nums)
        output = []

        for num, freq in count.items():
            buckets[freq].append(num)

        for i in range(n, -1, -1):

            for j in range(len(buckets[i])):

                output.append(buckets[i][j])

                if len(output) == k:
                    return output

        return output
        