class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
            if zero_cnt > 1: return [0] * len(nums)
            
        res = []
        for i, c in enumerate(nums):
            if zero_cnt:
                if c:
                    res.append(0)
                else:
                    res.append(prod)
            else:
                div = prod // c
                res.append(div)
        return res