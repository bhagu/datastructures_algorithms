def product_of_array_except_self(nums):
    output = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        output.append(product)
    return output


def product_of_array_except_self_best_method(nums):
    n = len(nums)
    output = [1] * n

    # Calculate the product of all elements to the left of each index
    left_product = 1
    for i in range(n):
        output[i] *= left_product
        left_product *= nums[i]

    # Calculate the product of all elements to the right of each index
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(product_of_array_except_self_best_method(nums))