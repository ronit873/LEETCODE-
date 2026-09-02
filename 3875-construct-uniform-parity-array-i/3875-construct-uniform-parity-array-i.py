class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        has_odd = any(x % 2 == 1 for x in nums1)
        has_even = any(x % 2 == 0 for x in nums1)

        # If all elements already have the same parity
        if not (has_odd and has_even):
            return True

        # We can make every element odd if there is at least
        # one even number to subtract from every odd number.
        if has_even:
            return True

        return False