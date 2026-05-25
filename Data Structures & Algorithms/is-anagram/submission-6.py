class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Separate Dictionaries for strings s and t
        seen_characters_s = {}
        seen_characters_t = {}

        # Set a key-value pair combination for each distinct character 
        for char in s:
            if char in seen_characters_s:
                # Increase 'value' by one for each additional occurence 
                # of that character
                seen_characters_s[char] += 1
            # If new character, set default value to one for first occurence
            else:
                seen_characters_s[char] = 1

        # Same logic as above 
        for char in t:
            if char in seen_characters_t:
                seen_characters_t[char] += 1
            else:
                seen_characters_t[char] = 1

        return seen_characters_s == seen_characters_t 

        # Additional Notes/Logic:
        """
        Future improvements:

        Since logically anagrams must be equivalent in string length, 
        an initial if statement testing if they are not the same size will 
        save runtime by potentially terminating the function early.

        The anagram question poses the problem that the strings could contain 
        the same characters in a different order, so resolving this via sorting 
        would just neccesitate a comparison between sorted strings. The space 
        complexity would be more efficient than a hashmap, but this implementation
        would have a O(nlogn) time complexity as supposed to O(s+t), something to
        consider when making tradeoffs based on the circumstance.
        """





        