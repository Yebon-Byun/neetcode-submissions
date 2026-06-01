"""
Trying
- heapify 적용된 heap 자료구조에서 큰 값을 두 개 빼는 방법? max_heap. 근데 구현이 잘 안되네?
  -> 리스트에 있는 값들을 음수로 모두 일단 적용시키고, heapify를 진행한다.

After solution
- max_heap 사용하니깐 -로 나와서 대소관계가 헷갈린다.
  
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x-y)
        
        stones.append(0)
        return abs(stones[0])

