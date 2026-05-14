class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)

        top = 0
        bottom = rows -1

        while (top<=bottom):
            mid = (top+bottom)//2 
            if matrix[mid][-1]<target:
                top= mid+1
            elif matrix[mid][0]>target:
                bottom = mid -1
            else:
                break
        if not(top<=bottom):
            return False

        left = 0
        right = cols-1
        row= (top+bottom)//2
        while left<= right :
            mid = (left+right)//2
            if matrix[row][mid]< target :
                left = mid+1
            elif matrix[row][mid]> target:
                right = mid - 1
            else:
                return True
        return False

        