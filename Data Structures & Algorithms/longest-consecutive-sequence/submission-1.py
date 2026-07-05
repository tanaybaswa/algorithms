class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        cons_map = {}

        current_max = 0

        for num in nums:

            if num in cons_map:
                continue

            value = 1

            if num + 1 in cons_map:
                value += cons_map[num + 1]

            cons_map[num] = value

            current_max = max(current_max, value)

            j = num

            while j - 1 in cons_map:

                new_val = cons_map[j - 1] + value

                current_max = max(current_max, new_val)

                cons_map[j - 1] = new_val
                j -= 1

        return current_max
        