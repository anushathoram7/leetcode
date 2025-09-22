class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            count = 0
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                count += 1
            return count

        nums = [(power(i), i) for i in range(lo, hi + 1)]
        nums.sort()
        return nums[k - 1][1]
