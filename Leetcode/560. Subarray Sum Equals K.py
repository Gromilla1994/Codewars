# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        s = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if sum(nums[i:j]) == k:
                    s += 1

        return s


obj = Solution()
print(obj.subarraySum([-1, -1, 1], 0))
