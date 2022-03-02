import stairs_recursive_solution


def test_case_1():
    s = stairs_recursive_solution.Solution()
    result = s.climbStairs(2)
    assert result == 2

def test_case_2():
    s = stairs_recursive_solution.Solution()
    result = s.climbStairs(3)
    assert result == 3
