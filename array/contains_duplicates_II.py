def contains_duplicates_ii(nums, k):
    seen = {}
    
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i

    return False

if __name__ == "__main__":
    nums = [1, 2, 3, 4 , 5, 12, 1]
    k = 3
    result = contains_duplicates_ii(nums, k)
    print(f"Contains duplicates within distance {k}: {result}")