class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            start = 0
            end = len(m) - 1
            
            if target in m:
                return True
        
        return False

            # if m[start] <= target and target <= m[end]:
            #     if target in m[start:]
                # print(m)
                # mid = (start + end) // 2
                
                
                # if m[mid] == target:
                #     return True

                # elif m[mid] > target:
                #     end = m[mid] - 1
                
                # elif m[mid] < target:
                #     start = m[mid] + 1

        return False



                        