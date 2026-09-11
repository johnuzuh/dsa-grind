# ======================================
# LeetCode Problem: group anagrams
# Language: python3
# Link: https://leetcode.com/problems/group-anagrams/
# Synced by: LinkCode
# Date: 9/11/2026, 6:50:47 PM
# ======================================


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            signature = "".join(sorted(str))
            if signature not in groups:
                groups[signature] = []
            groups[signature].append(str)
        return list (groups.values())