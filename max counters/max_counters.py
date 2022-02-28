# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):

    to_return = [0] * N
    current_max = 0
    for i in A:
        if i in range(1, N+1):
            to_return[i-1] += 1
            if to_return[i-1] > current_max:
                current_max = to_return[i-1]
        elif i == (N+1):
            for idx in range(0, len(to_return)):
                to_return[idx] = current_max

    return to_return

