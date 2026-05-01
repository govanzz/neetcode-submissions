class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        leftarr=[]
        rightarr=[]
        right =1 
        left =1 
        for i in range(len(nums)):
            leftarr.append(left)
            left*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            rightarr.append(right)
            right*=nums[i]
        rightarr.reverse()   
        for j in range(len(nums)):
            output.append(leftarr[j]*rightarr[j])
        return output

        

            

        