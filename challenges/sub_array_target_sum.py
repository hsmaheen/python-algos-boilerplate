# [2,4,-2,1,-3,5,-3], X = 5 --> Result = [2,4,-2,1]


def get_sub_array(nums, targetSum):
    if not nums or len(nums) == 0:
        return []

    prefixSum = 0
    sumDict = dict()

    for idx, num in enumerate(nums):

        prefixSum = prefixSum + num

        if prefixSum == targetSum:
            return [0, idx]

        if (prefixSum - targetSum) in sumDict:
            startIdx = sumDict.get(prefixSum - targetSum)
            return [startIdx + 1, idx]

        sumDict.update({prefixSum: idx})

    return []


nums = [2, 4, -2, 1, -3, 5, -3]
res = get_sub_array(nums, 3)

print(res)
