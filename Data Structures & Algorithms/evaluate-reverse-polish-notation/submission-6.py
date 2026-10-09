class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack=[]
        for i in tokens:
            if i=='+':
                x=numstack.pop()
                y=numstack.pop()
                ans=x+y
                numstack.append(ans)
            elif i=='-':
                y=numstack.pop()
                x=numstack.pop()
                ans=x-y
                numstack.append(ans)
            elif i=='*':
                x=numstack.pop()
                y=numstack.pop()
                ans=x*y
                numstack.append(ans)
            elif  i=='/':
                y=numstack.pop()
                x=numstack.pop()
                numstack.append(int(x/y))
            else:
                numstack.append(int(i))
        return int(numstack[-1])

                                                                                 

            

                                                                                  

                                                                                 

            

        