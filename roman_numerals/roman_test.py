import roman


def test_case_1():
    s = roman.Solution()
    result = s.romanToInt("MCMXCIV")
    assert result == 1994

def test_case_2():
    s = roman.Solution()
    result = s.romanToInt("DCXXI")
    assert result == 621




