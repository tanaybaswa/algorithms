class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """

        -1 0 1 2 -1 -4

        -4 -1 -1 0 1 2



        """

        n = len(nums)
        nums.sort()

        output = []

        for i in range(n - 2):

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            val = nums[i]
            target = -val

            j = i + 1
            k = n - 1

            while j < k:

                total = nums[j] + nums[k]

                if total > target:

                    while k > j and nums[k] == nums[k - 1]:
                        k -= 1

                    k -= 1

                elif total < target:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    j += 1

                elif total == target:
                    output.append([val, nums[j], nums[k]])
                    while k > j and nums[k] == nums[k - 1]:
                        k -= 1

                    k -= 1

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    j += 1


        return output
        