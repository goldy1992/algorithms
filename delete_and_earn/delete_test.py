import delete


def test_case_1():
    s = delete.Solution()
    input_val = [3,4,2]
    expected = 6
    result = s.deleteAndEarn(input_val)
    assert expected == result


def test_case_2():
    s = delete.Solution()
    input_val = [2, 2, 3, 3, 3, 4]
    expected = 9
    result = s.deleteAndEarn(input_val)
    assert expected == result


def test_case_3():
    s = delete.Solution()
    input_val = [8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4]
    expected = 61
    result = s.deleteAndEarn(input_val)
    assert expected == result


def test_case_4():
    s = delete.Solution()
    input_val = [6, 5, 10, 2, 8, 6, 6, 5, 2, 9, 9, 4, 6, 3, 3, 7, 7, 8, 9, 5]
    expected = 62
    result = s.deleteAndEarn(input_val)
    assert expected == result

