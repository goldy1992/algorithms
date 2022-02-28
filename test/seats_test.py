import seats

def test_case_1():
    result = seats.solution([1,4,1], [1,5,1])
    assert result == 2


def test_case_2():
    result = seats.solution([4,4,2,4], [5,5,2,5])
    assert result == 3


def test_case_3():
    result = seats.solution([2,3,4,2], [2,5,7,2])
    assert result == 2


