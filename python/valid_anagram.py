# ======================================
# LeetCode Problem: valid anagram
# Language: python3
# Link: https://leetcode.com/problems/valid-anagram/
# Synced by: LinkCode
# Date: 9/6/2026, 4:18:45 PM
# ======================================


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)