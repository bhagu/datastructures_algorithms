def top_k_frequent_elements(nums, k):

    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Sort the elements by frequency in descending order
    sorted_elements = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Return the top k frequent elements
    return [element[0] for element in sorted_elements[:k]]

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent_elements(nums, k))
