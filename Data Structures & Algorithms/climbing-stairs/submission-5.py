class Solution:
    def climbStairs(self, n: int) -> int:
        # n이 1 또는 2인 경우는 경우의 수가 n과 일치하므로 그대로 반환
        if n <= 2:
            return n

        # dp[i] = i번째 계단까지 도달하는 경우의 수
        dp = [0] * (n + 1)

        # 초기 조건(Base cases):
        # 1층: 1가지(1칸)
        # 2층: 2가지(1+1칸, 2칸)
        dp[1], dp[2] = 1, 2

        # 3층부터 n층까지 bottom-up 방식으로 테이블 채우기
        # 점화식: dp[i] = dp[i-2] + dp[i-1]
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        # 최정적으로 dp[n]이 구하고 싶은 값
        return dp[i]

    # Time Complexity: O(n)
    # Space Complexity: O(n)