class Solution:
    def binary_search(self, start, end, nums, target):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(mid + 1, end, nums, target)
        return self.binary_search(start, mid - 1, nums, target)
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)
        

        

