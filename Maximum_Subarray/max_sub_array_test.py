import max_sub_array


def test_case_1():
    s = max_sub_array.Solution()
    result = s.maxSubArray([5, 19, 8, 1])
    assert result == 33


def test_case_2():
    s = max_sub_array.Solution()
    result = s.maxSubArray([5,4,-1,7,8])
    assert result == 23


def test_case_3():
    s = max_sub_array.Solution()
    result = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert result == 6


def test_case_4():
    s = max_sub_array.Solution()
    result = s.maxSubArray([-1,1,2,1])
    assert result == 4




