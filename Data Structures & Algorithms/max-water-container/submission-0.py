class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights)-1
        left= 0
        maxarea=0
        while left<right:
            area= (right-left)* min(heights[left],heights[right])
            maxarea=max(maxarea,area)
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return maxarea
        