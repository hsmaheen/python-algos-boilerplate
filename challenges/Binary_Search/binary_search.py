def binary_search(nums, target):
    if not nums or not target:
        return False

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + round((end - start) / 2)
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return True
    return False
