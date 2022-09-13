class Solution:
    def romanToInt(self, s: str) -> int:
        hash_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_number = float("inf")
        for r in s:
            act_number = hash_table[r]
            if act_number <= prev_number:
                result += act_number
            else:
                result -= prev_number
                result += act_number - prev_number

            prev_number = act_number
        return result


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
