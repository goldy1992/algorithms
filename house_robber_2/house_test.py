import house as h


def test_case_1():
    s = h.Solution()
    cost = [2,3,2]
    expected = 3
    result = s.rob(cost)
    assert expected == result


def test_case_2():
    s = h.Solution()
    cost = [1,2,3,1]
    expected = 4
    result = s.rob(cost)
    assert expected == result


def test_case_3():
    s = h.Solution()
    cost = [1,2,3]
    expected = 3
    result = s.rob(cost)
    assert expected == result

def test_case_4():
    s = h.Solution()
    cost = [200, 3, 140, 20, 10]
    expected = 340
    result = s.rob(cost)
    assert expected == result

