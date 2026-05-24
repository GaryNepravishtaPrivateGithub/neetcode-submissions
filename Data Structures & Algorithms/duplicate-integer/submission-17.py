class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sort the array from smallest to largest
        nums.sort()

        # Avoid an 'Index out of Bounds' Error 
        # by using len(nums) - 1 for range
        for i in range(len(nums) - 1):
            # Due to sorting, equivalent numbers should be adjacent
            if nums[i] == nums[i + 1]:
                return True
        return False 

        # Additional Notes/Logic: 
        """ 
        When incrementing through array 'nums' in range(len(nums) - 1),
        the following comparison nums[i] == nums[i + 1] looks at the 
        second to last and last value of the array.

        Since the sorting algorithm causes duplicates to become adjacent,
        there is no need to iterate until the last element of the array
        """


        


        