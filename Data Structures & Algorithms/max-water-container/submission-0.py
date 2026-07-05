class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)

        l = 0
        r = n - 1

        area = 0

        while l < r:

            hl = heights[l]
            hr = heights[r]

            current_area = min(hl, hr) * (r - l)

            area = max(area, current_area)

            if hl < hr:
                l += 1

            else:
                r -= 1


        return area
        