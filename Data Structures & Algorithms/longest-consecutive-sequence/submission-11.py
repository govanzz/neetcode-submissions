class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        max_length=0
        for n in set1:
            if n-1 not in set1:
                current=n
                lenght=1
                while current+1 in set1:
                    current+=1
                    lenght+=1
                max_length=max(max_length,lenght)
        return max_length
