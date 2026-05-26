class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # If the complement has not been seen yet, store the current
        # number and its index for future complement checks
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            
            # Confirms the nums[i] + complement pair exists in nums
            if complement in seen:
                # Retrieve the index of the complement
                j = seen[complement]
                if i > j:
                    return [j, i]
                elif i < j:
                    return [i, j]

            # If there currently is no complement, add the current
            # number and its index into the hashmap for future lookups  
            seen[nums[i]] = i

        # Additional Notes/Logic:
        """
        Code Improvement: Since the dictionary 'seen' only stores previous 
        indices when iterating through the array, we can already deduce that 
        the complement's index pair j will always be before i (aka smaller).

        Because of this, we can skip the if statement comparisons and just 
        return a list of indices j then i (j represented as seen[complement])
        in the following return statement: 

        return [seen[complement], i]
        """


