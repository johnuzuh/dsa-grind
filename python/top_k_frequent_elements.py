# ======================================
# LeetCode Problem: top k frequent elements
# Language: python3
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Synced by: LinkCode
# Date: 9/15/2026, 3:53:49 PM
# ======================================


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        sorted_counts = sorted(counts, key=counts.get, reverse = True)

        return sorted_counts[:k]