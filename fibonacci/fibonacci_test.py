import fibonacci


def test_case_1():
    s = fibonacci.Solution()
    result = s.fib(0)
    assert 0 == result


def test_case_2():
    s = fibonacci.Solution()
    result = s.fib(1)
    assert 1 == result


def test_case_3():
    s = fibonacci.Solution()
    result = s.fib(2)
    assert 1 == result


def test_case_3():
    s = fibonacci.Solution()
    result = s.fib(3)
    assert 2 == result


def test_case_4():
    s = fibonacci.Solution()
    result = s.fib(4)
    assert 3 == result


