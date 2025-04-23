class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = [0] * 40
        max_count = 0

        for i in range(1, n + 1):
            digit_sum = sum(int(c) for c in str(i))
            freq[digit_sum] += 1
            max_count = max(max_count, freq[digit_sum])

        return sum(1 for x in freq if x == max_count)