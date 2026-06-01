class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates = sorted(candidates)
        print(candidates)

        def dfs(i, curr, total):
            if total == target and not curr.copy() in res:
                    res.append(curr.copy())

            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
        

        dfs(0, [], 0)
        return res