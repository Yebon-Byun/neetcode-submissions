"""
Boolean Array

[Intuition]:
The answer must be in the range [1, n+1]
so we only care about numbers from 1 to n. We create a boolean array of size n where seen[i] tells us whether i+1 exists in the input. Then we just find the first index that's still false.

[Algorithm]:
1. Create a boolean array seen of size n, initialized to false.
2. For each number in the input:
    if it's between 1 and n, mark seen[num - 1] = true
3. Scan seen from index 0 to n-1
    return i+1 for the first false entry
4. if all entries are true, return n+1

"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * n
        for num in nums: 
            if num > 0 and num <= n:
                seen[num - 1] = True

        for num in range(1, n+1):
            if not seen[num-1]:
                return num
        
        return n+1

# time: O(n)
# space; O(n)


"""
['seen[num-1]' num-1 인 이유]:
값의 세계는 1부터 시작하는데 인덱스의 세계는 0부터 시작해서
seen의 각 칸은 "그 번호가 출석했나"를 담는 사물함인데, 담고 싶은 번호는 1부터 n까지 n개이고, 가진 칸은 인덱스 0부터 n-1까지 n개예요. 개수는 딱 맞는데 번호가 한 칸씩 어긋나 있으니, "번호 v의 사물함 = 칸 v-1"로 배정한 거예요

"""
                