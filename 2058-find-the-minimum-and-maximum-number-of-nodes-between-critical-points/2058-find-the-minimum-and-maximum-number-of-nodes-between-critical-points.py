class Solution:
    def nodesBetweenCriticalPoints(self, head):
        first = prev = None
        min_dist = float('inf')
        max_dist = 0
        index = 1

        while head and head.next:
            if prev is not None:
                is_critical = (
                    (prev < head.val and head.val > head.next.val) or
                    (prev > head.val and head.val < head.next.val)
                )

                if is_critical:
                    if first is None:
                        first = index
                    else:
                        min_dist = min(min_dist, index - prev_critical)
                        max_dist = index - first

                    prev_critical = index

            prev = head.val
            head = head.next
            index += 1

        if min_dist == float('inf'):
            return [-1, -1]

        return [min_dist, max_dist]