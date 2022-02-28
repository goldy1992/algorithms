import max_counters


def test_case_1():
    result = max_counters.solution(1, [1])
    assert result == [1]


def test_case_2():
    result = max_counters.solution(5, [3, 4, 4, 6, 1, 4, 4])
    assert result == [3, 2, 2, 4, 2]