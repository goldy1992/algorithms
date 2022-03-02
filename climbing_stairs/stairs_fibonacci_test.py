import stairs_fibonacci_solution as f


def test_case_1():
    s = f.Solution()
    result = s.climbStairs(2)
    assert result == 2

def test_case_2():
    s = f.Solution()
    result = s.climbStairs(3)
    assert result == 3
