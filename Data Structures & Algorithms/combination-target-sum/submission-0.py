"""
nums = [2,3,6,7]
target = 7

Start: dfs(0, [], 0)
├── pick 2 → dfs(0, [2], 2)
│   ├── pick 2 → dfs(0, [2,2], 4)
│   │   ├── pick 2 → dfs(0, [2,2,2], 6)
│   │   │   ├── pick 2 → dfs(0, [2,2,2,2], 8) ❌ over
│   │   │   └── skip 2 → dfs(1, [2,2,2], 6)
│   │   │       ├── pick 3 → dfs(1, [2,2,2,3], 9) ❌ over
│   │   │       └── skip 3 → dfs(2, [2,2,2], 6)
│   │   │           ├── pick 6 → dfs(2, [2,2,2,6], 12) ❌
│   │   │           └── skip 6 → dfs(3, [2,2,2], 6)
│   │   │               ├── pick 7 → dfs(3, [2,2,2,7], 13) ❌
│   │   │               └── skip 7 → dfs(4, [2,2,2], 6) ❌ end
│   │   └── skip 2 → dfs(1, [2,2], 4)
│   │       ├── pick 3 → dfs(1, [2,2,3], 7) ✅ ✔
│   │       │   ├── pick 3 → dfs(1, [2,2,3,3], 10) ❌
│   │       │   └── skip 3 → dfs(2, [2,2,3], 7)
│   │       │       ├── pick 6 → dfs(2, [2,2,3,6], 13) ❌
│   │       │       └── skip 6 → dfs(3, [2,2,3], 7)
│   │       │           ├── pick 7 → dfs(3, [2,2,3,7], 14) ❌
│   │       │           └── skip 7 → dfs(4, [2,2,3], 7) ❌
│   │       └── skip 3 → dfs(2, [2,2], 4)
│   │           ├── pick 6 → dfs(2, [2,2,6], 10) ❌
│   │           └── skip 6 → dfs(3, [2,2], 4)
│   │               ├── pick 7 → dfs(3, [2,2,7], 11) ❌
│   │               └── skip 7 → dfs(4, [2,2], 4) ❌
│   └── skip 2 → dfs(1, [2], 2)
│       ├── pick 3 → dfs(1, [2,3], 5)
│       │   ├── pick 3 → dfs(1, [2,3,3], 8) ❌
│       │   └── skip 3 → dfs(2, [2,3], 5)
│       │       ├── pick 6 → dfs(2, [2,3,6], 11) ❌
│       │       └── skip 6 → dfs(3, [2,3], 5)
│       │           ├── pick 7 → dfs(3, [2,3,7], 12) ❌
│       │           └── skip 7 → dfs(4, [2,3], 5) ❌
│       └── skip 3 → dfs(2, [2], 2)
│           ├── pick 6 → dfs(2, [2,6], 8) ❌
│           └── skip 6 → dfs(3, [2], 2)
│               ├── pick 7 → dfs(3, [2,7], 9) ❌
│               └── skip 7 → dfs(4, [2], 2) ❌
└── skip 2 → dfs(1, [], 0)
    ├── pick 3 → dfs(1, [3], 3)
    │   ├── pick 3 → dfs(1, [3,3], 6)
    │   │   ├── pick 3 → dfs(1, [3,3,3], 9) ❌
    │   │   └── skip 3 → dfs(2, [3,3], 6)
    │   │       ├── pick 6 → dfs(2, [3,3,6], 12) ❌
    │   │       └── skip 6 → dfs(3, [3,3], 6)
    │   │           ├── pick 7 → dfs(3, [3,3,7], 13) ❌
    │   │           └── skip 7 → dfs(4, [3,3], 6) ❌
    │   └── skip 3 → dfs(2, [3], 3)
    │       ├── pick 6 → dfs(2, [3,6], 9) ❌
    │       └── skip 6 → dfs(3, [3], 3)
    │           ├── pick 7 → dfs(3, [3,7], 10) ❌
    │           └── skip 7 → dfs(4, [3], 3) ❌
    └── skip 3 → dfs(2, [], 0)
        ├── pick 6 → dfs(2, [6], 6)
        │   ├── pick 6 → dfs(2, [6,6], 12) ❌
        │   └── skip 6 → dfs(3, [6], 6)
        │       ├── pick 7 → dfs(3, [6,7], 13) ❌
        │       └── skip 7 → dfs(4, [6], 6) ❌
        └── skip 6 → dfs(3, [], 0)
            ├── pick 7 → dfs(3, [7], 7) ✅ ✔
            │   ├── pick 7 → dfs(3, [7,7], 14) ❌
            │   └── skip 7 → dfs(4, [7], 7) ❌
            └── skip 7 → dfs(4, [], 0) ❌

"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            dfs(i+1, curr, total)

        dfs(0, [], 0)

        return res
