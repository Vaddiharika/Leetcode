class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        sum, maxi, mini = 0, 0, 0
        for x in differences:
            sum += x
            maxi = max(maxi, sum)
            mini = min(mini, sum)
        return max(0, upper - lower - maxi + mini + 1)