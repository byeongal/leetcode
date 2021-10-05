class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        left, right = 0, 1
        used_alpha = set()
        used_alpha.add(s[left])
        answer = 1
        while right < len(s):
            while left != right and s[right] in used_alpha:
                used_alpha.remove(s[left])
                left += 1
            used_alpha.add(s[right])
            answer = max(answer, len(used_alpha))
            right += 1
        return answer