from sub_array_target_sum import get_sub_array


class TestSubArrayTargetSum:

    """
    Should return the result when sum starts at in between
    """

    def test_return_result(self):
        nums = [2, 4, -2, 1, -3, 5, -3]
        target = 3
        res = get_sub_array(nums, target)
        assert res == [1, 3]

    """
       Should return the [] when sum is not present
    """

    def test_return_nothing(self):
        nums = [2, 4, -2, 1, -3, 5, -3]
        target = 23
        res = get_sub_array(nums, target)
        assert res == []

    """
       Should return the result when sum starts at idx 0
    """

    def test_retur_result_two(self):
        nums = [2, 4, -2, 1, -3, 5, -3]
        target = 6
        res = get_sub_array(nums, target)
        assert res == [0, 1]
