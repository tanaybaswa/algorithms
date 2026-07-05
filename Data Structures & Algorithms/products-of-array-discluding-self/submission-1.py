class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums.count(0) >= 2:
            return [0 for _ in range(len(nums))]

        if nums.count(0) == 1:
            product = math.prod([num for num in nums if num != 0])

            result = []
            for num in nums:
                if num == 0:
                    result.append(product)

                else:
                    result.append(0)

            return result

        product = math.prod([num for num in nums])

        result = [int(product/x) for x in nums]

        return result
        