import factories

def test_case_1():
    result = factories.solution([5, 19, 8, 1])
    assert result == 3

def test_case_2():
    result = factories.solution([10, 10])
    assert result == 2

def test_case_3():
    result = factories.solution([3 , 0 , 5])
    assert result == 2

def test_case_3():
    result = factories.solution([30000])
    assert result == 1

def test_case_3():
    result = factories.solution([30001, 2])
    assert result == 2
