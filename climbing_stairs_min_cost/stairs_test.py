import stairs as f


def test_case_1():
    s = f.Solution()
    cost = [10,15,20]
    expected = 15
    result = s.minCostClimbingStairs(cost)
    assert expected == result

def test_case_2():
    s = f.Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    expected = 6
    result = s.minCostClimbingStairs(cost)
    assert expected == result
