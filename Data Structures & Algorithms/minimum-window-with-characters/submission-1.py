class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left =0
        need = {}
        window = {}
        for char in t:
            need[char]=need.get(char,0)+1
        
        lengthr = float('inf')
        result = [-1,1]
        have=0
        needcount=len(need)

        for right in range(len(s)):
            char = s[right]
            window[char]=window.get(char,0)+1
            if char in need and window[char]==need[char]:
                have+=1
            while have == needcount:
                if  right- left+1 < lengthr:
                    result = [left,right]
                    lengthr = right-left+1
                
                left_char= s[left]
                window[left_char]-=1
                if left_char in need and window[left_char]<need[left_char]:
                    have-=1
                left+=1
        left,right = result
        if lengthr==float('inf'):
            return ""
        else:
            return s[left:right+1]
                    



        
        