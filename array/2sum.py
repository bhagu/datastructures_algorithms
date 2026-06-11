def two_sum(nums, target):

    for i in range(len(nums)-1):
        if nums[i] + nums[i+1] == target:
            return i, i+1

def two_sum_revised(nums, target):

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i] + nums [j] == target:
                return i, j

def two_sum_revised_big_o_n(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 13
    result = two_sum_revised_big_o_n(nums, target)
    print(f"Result: {result}")

