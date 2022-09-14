class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0
        for n in accounts:
            summed = sum(n)
            highest = max(highest, summed)
        return highest
