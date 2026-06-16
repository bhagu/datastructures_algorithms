def contains_duplicates(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 12]
    result = contains_duplicates(nums)
    print(f"Contains duplicates: {result}")