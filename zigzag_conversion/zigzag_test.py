import zigzag


def test_case_1():
    string = "PAYPALISHIRING"
    numRows = 3
    expected = "PAHNAPLSIIGYIR"
    s = zigzag.Solution()
    result = s.convert(string, numRows)
    assert expected == result


def test_case_2():
    string = "PAYPALISHIRING"
    numRows = 4
    expected = "PINALSIGYAHRPI"
    s = zigzag.Solution()
    result = s.convert(string, numRows)
    assert expected == result

def test_case_3():
    string = "ABCD"
    numRows = 2
    expected = "ACBD"
    s = zigzag.Solution()
    result = s.convert(string, numRows)
    assert expected == result


