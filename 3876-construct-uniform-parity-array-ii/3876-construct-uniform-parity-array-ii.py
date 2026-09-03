class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        has_odd = any(x % 2 for x in nums1)
        has_even = any(x % 2 == 0 for x in nums1)

        # All already have the same parity
        if not (has_odd and has_even):
            return True

        # To make everything odd:
        # every even number needs an odd smaller number.
        # To make everything even:
        # every odd number needs an odd smaller number (impossible
        # for the smallest odd), so check using the smallest element.
        
        mn = min(nums1)

        # If minimum is odd, we can make every even number odd
        # by subtracting the minimum.
        if mn % 2 == 1:
            return True

        # If minimum is even, an odd number cannot be made even,
        # because there is no smaller odd guaranteed.
        # We need every odd number to have a smaller odd number.
        smallest_odd = min((x for x in nums1 if x % 2), default=None)

        if smallest_odd is None:
            return True

        for x in nums1:
            if x % 2 == 1 and x == smallest_odd:
                # Smallest odd must remain odd.
                continue

        # We can make all even only if there are no odd numbers.
        return False