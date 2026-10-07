class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=nums1+nums2
        s.sort()
        if len(s)%2!=0:
            return float(s[len(s)//2])
        else:
            a1=s[len(s)//2-1]
            a2=s[(len(s)//2)]
            return (a1+a2)/2


        