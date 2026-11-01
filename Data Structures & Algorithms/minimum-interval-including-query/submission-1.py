class Solution:
 def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    # Sort intervals from shortest to longest.
    # Adding 1 would not change their sorting order.
    intervals.sort(key=lambda x: x[1] - x[0])

    # Store (query value, original index), then sort by query value.
    # Example: [5, 2, 4] becomes [(2, 1), (4, 2), (5, 0)].
    ordered = sorted((q, i) for i, q in enumerate(queries))

    # Number of queries.
    n = len(queries)

    # Default answer is -1: no interval covers the query.
    res = [-1] * n

    # Each position initially points to itself.
    # The extra position n means "no unanswered queries remain."
    parent = list(range(n + 1))

    # Return the next unanswered position at or after i.
    def find(i):
        # If i points elsewhere, it has already been answered.
        while i != parent[i]:
            # Shorten the chain so future searches are faster.
            parent[i] = parent[parent[i]]

            # Follow the pointer forward.
            i = parent[i]

        # This position is unanswered, or it is the ending position n.
        return i

    # Process each interval, shortest first.
    for start, end in intervals:
        # Search across the sorted queries.
        left, right = 0, n - 1

        # Binary search for the first query >= start.
        while left <= right:
            mid = (left + right) // 2

            # This query is too small to be inside the interval.
            if ordered[mid][0] < start:
                left = mid + 1

            # This query might work; look for an earlier one.
            else:
                right = mid - 1

        # left is the first position whose query is >= start.
        # Skip it if it has already been answered.
        i = find(left)

        # Answer queries while they are within this interval.
        # Their values are already >= start.
        while i < n and ordered[i][0] <= end:
            # Recover this query's index in the original input.
            original_index = ordered[i][1]

            # Save the interval's inclusive length.
            res[original_index] = end - start + 1

            # Mark position i answered by pointing to the next
            # unanswered position.
            parent[i] = find(i + 1)

            # Move to that next unanswered position.
            i = parent[i]

    # Answers are already stored in the original query order.
    return res