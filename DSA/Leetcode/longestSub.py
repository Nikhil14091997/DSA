class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        else:
            i, j = 0, 1
            maxSub = 1
            while i < j and j < len(s):
                if s[j] not in s[i:j]:
                    maxSub = max(maxSub, len(s[i:j+1]))
                    print(f"MaxSofar: maxSub = {maxSub}, current = {s[i:j+1]}")
                    j += 1
                else:
                    i = i+1
                    j = i+1
            return maxSub
            

obj = Solution()
s = "abcabcbb"
print(obj.lengthOfLongestSubstring(s))