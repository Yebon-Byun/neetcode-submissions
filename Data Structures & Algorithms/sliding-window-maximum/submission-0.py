class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for curr in range(len(nums) - k + 1):
            curr_win = nums[curr:curr + k]
            print(curr_win)
            max_win = max(curr_win)
            res.append(max_win)
        return res
            
