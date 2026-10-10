class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s=s+str(i)
        l=int(s)+1
        x=str(l)
        m=list(x)
        return m
        