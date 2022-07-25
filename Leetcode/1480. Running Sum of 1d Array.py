# Given an array nums. We define a running sum of an array
# as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        new_arr = []
        for i in range(len(nums)):
            new_arr.append(nums[i] + sum(nums[:i]))
        return new_arr


obj = Solution()

print(obj.runningSum([1, 2, 3, 4]))
