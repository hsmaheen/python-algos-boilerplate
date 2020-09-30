from binary_search import binary_search


class TestBinarySearch:
    def test_valid_inputs(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        result = binary_search(nums, target)
        assert result is True

    def test_invalid_inputs(self):
        nums = [1, 2, 3, 4, 5]
        target = 7
        result = binary_search(nums, target)
        assert result is False

    def test_null_array_input(self):
        nums = []
        target = 7
        result = binary_search(nums, target)
        assert result is False

    def test_null_target_inputs(self):
        nums = []
        target = None
        result = binary_search(nums, target)
        assert result is False
