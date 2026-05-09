class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1= set(nums)
        maxlen=0
        for n in set1:
            if n-1 not in set1:
                current = n
                length=1
                while current+1 in set1:
                    length+=1
                    current+=1
                maxlen=max(maxlen,length)
        return maxlen
        