class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0 
        e = len(matrix)-1
        while s <= e:
            m = (s + e)//2
            if matrix[m][0] == target:
                return True
            elif target < matrix[m][0]:
                e = m - 1
            elif target > matrix[m][0] and target <= matrix[m][-1]:
                l, h = 0, len(matrix[m])-1
                while l <= h:
                    mid = (l + h)//2
                    if matrix[m][mid] == target:
                        return True
                    elif matrix[m][mid] < target:
                        l = mid + 1
                    else:
                        h = mid - 1
                return False
            else:
                s = m + 1
        return False
