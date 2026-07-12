class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:

            print(f"left:{l} right:{r}")

            mid = (l + r)//2

            print(f"Mid Index: {mid} Mid Value: {nums[mid]}")

            if target == nums[mid]:
                return mid

            #left side is sorted for sure
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                #right side is sorted for sure
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
        