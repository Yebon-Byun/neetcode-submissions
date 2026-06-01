

"""
Give a shot
- input은 [1, 2, 3, 3] 들어갔는데 output에서는 안보인다 어디간걸까?
- heapq.heappush(self.heap, val)
  TypeError: heappush() argument 1 must be list, not None
  -> heapify는 변수에 할당하지 않고 해당 리스트에 적용시키면 그대로 변한다.
  -> 할당시켜서 프린트를 하면 'None'이 리턴된다.

- 첫 번째 예시는 통과했는데, 다른 히든 케이스는 통과를 못했다. 
- 사실 add 매서드가 무엇을 하는지 등 문제의 요구가 무엇인지 전반을 이해하지 못했다.
- 막히는 아래 예시는 heapify를 해도 정렬이 안된다. -> [2, 4, 8, 5] 이렇게 나옴
  ["KthLargest", [3, [4, 5, 8, 2]], 
  "add", [3], "add", [5], "add", [10], "add", [9], "add", [4]]

After solution
- 


2. Min-Heap
Time comp: O(m * log k)
Space comp: O(k)
"""



class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
