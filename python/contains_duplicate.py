# ======================================
# LeetCode Problem: contains duplicate
# Language: python3
# Link: https://leetcode.com/problems/contains-duplicate/
# Synced by: LinkCode
# Date: 9/7/2026, 7:03:48 PM
# ======================================


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


