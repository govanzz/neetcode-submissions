class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half = total//2
        A = nums1
        B = nums2
        if len(A)>len(B):
            A,B= B,A
        left = 0 
        right = len(A)-1
        
        while True:
            i= (left+right)//2
            j= half - i -2
            Aleft = A[i] if i>=0 else float("-inf")
            Aright= A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j>=0 else float ("-inf")
            Bright= B[j+1] if j+1 < len(B) else float("inf")

            if Bright >= Aleft and Bleft<= Aright:
                if total % 2 != 0:
                    return  min(Bright,Aright)
                else:
                    return (min(Bright, Aright)+ max( Bleft,Aleft))/2
            elif Bright < Aleft:
                right = i-1
            else:
                left = i+1
                  
                    
                
            