class Solution:
    def hammingWeight(self, n: int) -> int:
        x=bin(n)
        x1=str(x)
        l=x1.count("1")
        return l


        