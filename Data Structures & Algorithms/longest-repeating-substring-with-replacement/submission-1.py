class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        left=0
        maxf = 0
        for right in range(len(s)):
            char = s[right]
            count[char]=count.get(char,0)+1
            maxf=max(count[char],maxf)
            length = right-left + 1
            if length-maxf > k:
                count[s[left]]-=1
                left+=1
            res= max(res,right-left+1)
        return res
                 
                