class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        length_s1= len(s1)
        s1_count={}
        window_count={}
        left = 0
        for char in s1:
            s1_count[char]= s1_count.get(char,0)+1
        for right in range(len(s2)):
            char = s2[right]
            window_count[char]= window_count.get(char,0)+1
            if right - left + 1 > length_s1:
                left_char =  s2[left]
                window_count[left_char]-=1
                if window_count[left_char]==0:
                    del window_count[left_char] 
            
                left+=1

            if window_count== s1_count:
                return True
        return False
        
        