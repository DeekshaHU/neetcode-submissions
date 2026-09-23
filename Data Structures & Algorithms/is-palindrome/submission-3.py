class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s: 
            if i!=" " and i!='?' and i!="!" and i!="." and i!="$" and i!=',' and i!="'" and i!=":":
                a=a+i.lower()
        if a==a[::-1]:
            return True
        return False
        