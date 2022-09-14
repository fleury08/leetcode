class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		r_arr = sorted(ransomNote)
		m_arr = sorted(magazine)
		print(r_arr, m_arr)

print(Solution().canConstruct("aab", "baa"))