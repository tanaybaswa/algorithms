class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Pass 1: Build prefix products directly into result
        # result[i] will store the product of all numbers to the left of i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Multiply by suffix products on the fly from right to left
        # suffix will track the product of all numbers to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result