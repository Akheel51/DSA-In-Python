class Solution:
    def maxNumberOfBalloons(self, s: str) -> int:
        return min(s.count('b'), s.count('a'), s.count('l')//2, s.count('o')//2, s.count('n'))