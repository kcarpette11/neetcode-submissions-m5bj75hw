from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            y = stones.pop()  # largest
            x = stones.pop()  # second largest

            if x != y:
                target = y - x

                # binary search for insertion index
                left, right = 0, len(stones) - 1

                while left <= right:
                    mid = left + (right - left) // 2

                    if stones[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

                stones.insert(left, target)

        return stones[0] if stones else 0



        