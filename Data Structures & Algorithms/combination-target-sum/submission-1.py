class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        output = []
        n = len(nums)
        nums.sort()

        def f(i, t, path):

            if t == 0:
                output.append(path)

            for j in range(i, n):

                if t - nums[j] >= 0:
                    f(j, t - nums[j], path + [nums[j]])

                else:
                    break


        f(0, target, [])

        return output

        