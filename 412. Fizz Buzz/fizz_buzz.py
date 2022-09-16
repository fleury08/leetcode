from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz = []
        for i in range(1, n+1):
            fizzbuzz.append("")
            if not (i % 3):
                fizzbuzz[i-1] += "Fizz"
            if not (i % 5):
                fizzbuzz[i-1] += "Buzz"
            if i%3 and i%5:
                fizzbuzz[i-1] += str(i)
        return fizzbuzz

print(Solution().fizzBuzz(15))