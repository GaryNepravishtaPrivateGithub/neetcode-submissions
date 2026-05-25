class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Intialize a list for a future pair of indices
        indices_pair = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    # Index i is confirmed to be unequal to index j
                    # as the for loop naturally looks for subsequent indices
                    indices_pair.append(i)
                    indices_pair.append(j)

                    return indices_pair

        # Additional Notes/Logic:
        """
        Brute-force nested for loop approach: 
        O(n^2) time and O(1) space complexity

        For future reference, in python we can just return [i, j] 
        instead of initializing a index list and appending values.
        """
