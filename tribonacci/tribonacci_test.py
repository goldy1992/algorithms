import tribonacci


def test_case_1():
    s = tribonacci.Solution()
    result = s.tribonacci(0)
    assert 0 == result


def test_case_2():
    s = tribonacci.Solution()
    result = s.tribonacci(1)
    assert 1 == result


def test_case_3():
    s = tribonacci.Solution()
    result = s.tribonacci(2)
    assert 1 == result


def test_case_3():
    s = tribonacci.Solution()
    result = s.tribonacci(3)
    assert 2 == result


def test_case_4():
    s = tribonacci.Solution()
    result = s.tribonacci(4)
    assert 4 == result


