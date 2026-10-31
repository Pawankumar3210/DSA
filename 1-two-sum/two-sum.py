#Note to myself: I didn't solve this. I just was testing LeetCode's connection with GitHub using LeetSync and it was successful! Can't wait to begin my LeetCode journey soon....

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store the number as the key and its index as the value
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the required number to reach the target
            complement = target - num
            
            # Check if the complement is already in our dictionary
            if complement in num_to_index:
                # Return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # Otherwise, store the current number and its index in the dictionary
            num_to_index[num] = index

