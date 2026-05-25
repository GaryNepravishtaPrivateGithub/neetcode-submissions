class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize a set of unique elements
        seen_digits = set()

        # Add every unique element into the set (duplicates are not added)
        for integer in nums:
            seen_digits.add(integer)
        
        # If there are duplicates, seen_digits will have the same 
        # unique elements but less total elements, thus returning True
        # otherwise return False if the comparison evaluates to False
        return len(nums) != len(seen_digits)

        # Additional Notes/Logic:
        """
        For future reference, len(set(nums)) automatically initializes 
        a set of unique numbers from the array nums, thus reducing the
        need for a manual loop.

        Final return statement would just look like the following:
        return len(nums) != len(set(nums))
        """