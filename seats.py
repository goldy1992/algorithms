def solution(P, S):
    total_people = sum(P)

    idx = 0
    S.sort(reverse=True)
    seats_filled = 0
    while seats_filled < total_people:
        seats_filled += S[idx]
        idx += 1

    return idx
