class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        # 이렇게 하면 courses 개수에 맞게 그리고 각 courses의 pre-requisites이 업데이트 되는건가?


        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if pre_map[crs] == []:
                return True

            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            pre_map[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True