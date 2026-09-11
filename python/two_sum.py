# ======================================
# LeetCode Problem: two sum
# Language: python3
# Link: https://leetcode.com/problems/two-sum/
# Synced by: LinkCode
# Date: 9/11/2026, 4:25:42 PM
# ======================================


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       sum = {}
       for i, num in enumerate(nums):
        complement = target - num
        if complement in sum:
            return[sum[complement],i]
        sum[num] = i
