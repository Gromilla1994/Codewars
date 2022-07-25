# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly
# to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is
# 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_left = 0
        sum_right = sum(nums[1:])
        for i in range(len(nums)):
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
            sum_right -= nums[i+1] if i+1 != len(nums) else 0
        return -1


sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
