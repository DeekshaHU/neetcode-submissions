class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        d=sorted(dict,key=dict.get,reverse=True);
        return d[:k]
        
        

        