class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for l in magazine:
            if l in magazine_dict.keys():
                magazine_dict[l] += 1
            else:
                magazine_dict[l] = 1

        for n in ransomNote:
            if n not in magazine_dict or magazine_dict[n] == 0:
                return False
            magazine_dict[n] -= 1
        return True


print(Solution().canConstruct("aab", "baa"))
print(Solution().canConstruct("ab", "baa"))
print(Solution().canConstruct("cab", "baa"))
