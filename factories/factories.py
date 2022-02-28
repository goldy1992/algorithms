# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    total_pollution = sum(A)
    target = total_pollution / 2
    amount_reduced = 0
    num_filters = 0

    while amount_reduced < target:
        A.sort(reverse=True)
        reduced = A[0] / 2
        A[0] = reduced
        amount_reduced += reduced
        num_filters += 1

        if amount_reduced >= target:
            return num_filters

    # write your code in Python 3.6
    pass
