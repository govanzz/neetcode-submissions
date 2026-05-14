from math import ceil 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left<= right:
            hours = 0
            mid = (left+right)//2
            for pile in piles:
                hours+=ceil(pile/mid)
            if hours <= h:
                answer = mid 
                right=mid-1
            else:
                left = mid +1
        return answer
        

        