class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        while k > 0:
            res = -heapq.heappop(nums)
            print(k, res)
            k -= 1
        return res