class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            x=sorted(i)
            j=str(x)
            if j not in dict:
                dict[j]=[]
            dict[j].append(i)
        a=[]
        for key,values in dict.items():
            a.append(values)
        return a

        