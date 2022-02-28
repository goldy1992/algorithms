import pytest
import forum

def test_case_1():

    result = forum.solution("Codility We test coders", 14)
    assert result == "Codility We"


def test_case_2():
    result = forum.solution("Why Not", 100)
    assert result == "Why Not"

def test_case_3():
    result = forum.solution("The quick brown fox jumps over the lazy dog", 39)
    assert result == "The quick brown fox jumps over the lazy"

def test_case_4():
    result = forum.solution("Thequickbrownfoxumpsoverthelazydog", 1)
    assert result == ""



