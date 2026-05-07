class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        have=0
        need = {}
        window = {}
        needlength = 0
        res=float('inf')
        resl=[-1,1]
        left=0
        for char in t:
            need[char]=need.get(char,0)+1
        needlength= len(need)
        for right in range(len(s)):
            char=s[right]
            window[char]=window.get(char,0)+1

            if char in need and window[char]==need[char]:
                have+=1
            
            while have==needlength:

                if right-left+1<res:
                    resl=[left,right]
                    res=right-left+1
                left_char=s[left]
                window[left_char]-=1
                if left_char in need and window[left_char]<need[left_char]:
                    have-=1
                
                left+=1
        left,right= resl
        if res==float("inf"):
            return ""
        else:
            return s[left:right+1]





        