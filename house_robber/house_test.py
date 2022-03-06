import house as h


def test_case_1():
    s = h.Solution()
    cost = [1,2,3,1]
    expected = 4
    result = s.rob(cost)
    assert expected == result

def test_case_2():
    s = h.Solution()
    cost = [2,7,9,3,1]
    expected = 12
    result = s.rob(cost)
    assert expected == result
