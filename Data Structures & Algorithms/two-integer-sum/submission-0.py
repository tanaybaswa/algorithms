class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i, num in enumerate(nums):

            needed = target - num

            if needed in map:
                return [map[needed], i]

            map[num] = i

        return [0]




        