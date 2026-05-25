class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize a set (unique elements)
        seen_digits = set()

        # Iterating through elements in list instead of indices
        for integer in nums:
            if integer in seen_digits:
                return True
            seen_digits.add(integer)

        return False 

        # Additional Notes/Logic:
        """
        Using a set is more efficient than a dictionary/hashmap for
        this problem, due to the fact that we are only concerning 
        ourselves with unique values rather than pairs (saves memory).

        Differences between Lists, Tuples, and Sets:
        - Sets: Are mutable, but are only concerned with unique elements
        (as such do not allow for duplicates, ordering, or indexing/slicing)
        - Tuples: Are immutable (cannot change after creation), but allow for 
        duplicates, ordering, and indexing/slicing
        - Lists: Are all the above (mutable, and allow duplicates, ordering, and
        indexing/slicing)

        Definitions:
        - Ordered: Maintains sequence after insertion/creation
        - Heterogenous: Can allow for a mix of data types
        """


        


        