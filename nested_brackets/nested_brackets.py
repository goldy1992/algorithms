# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

open_bracket = set(['(', '{', '['])
close_bracket = set([')', '}', ']'])


def match(left, right):
    if left == '(':
        return right == ')'
    if left == '[':
        return right == ']'
    if left == '{':
        return right == '}'
    return False


def solution(S):
    # write your code in Python 3.6

    stack = []
    if len(S) == 0:
        return 1

    for c in S:
        if c in open_bracket:
            stack.append(c)
        elif c in close_bracket:
            if len(stack) == 0:
                return 0
            v = stack.pop()
            if not match(v, c):
                return 0

    return 1 if len(stack) == 0 else 0