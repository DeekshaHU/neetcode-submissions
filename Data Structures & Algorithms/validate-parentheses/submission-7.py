class Solution:
    def isValid(self, s: str) -> bool:
        n=[]
        for i in s:
            if i=="[" or i=="{" or i=="(":
                n.append(i)

            else:
                if not n:
                    return False
                x=n.pop()
                if  (x=="{" and i!="}")  or  (x=="[" and i!="]") or x=="(" and i!=")":
                    return False
    
        return len(n)==0


        