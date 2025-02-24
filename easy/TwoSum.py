def twoSum(nums, target):
    # Create a hash map to store the number and its index
    num_map = {}

    # Loop through the list
    for i, num in enumerate(nums):
        complement = target - num

        # If the complement exists in the hash map, return the indices
        if complement in num_map:
            return [num_map[complement], i]

        # Otherwise, store the current number with its index
        num_map[num] = i
