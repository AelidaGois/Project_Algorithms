def find_duplicate(nums):
    if not isinstance(nums, list) or not nums:
        return False
    nums.sort()
    prev_num = nums[0]
    for num in nums[1:]:
        if num == prev_num:
            return num
        prev_num = num
    return False
