def get_change(M, P):
    expected_val = float(M - P)
    change = 0
    # 1, 5, 10, 25, 50 ,100
    coins = [0, 0, 0, 0, 0, 0]

    while round(change, 2) < expected_val:
        if round((change + 1), 2) <= expected_val:
            coins[5] += 1
            change += 1
        elif round((change + 0.5), 2) <= expected_val:
            coins[4] += 1
            change += 0.5
        elif round((change + 0.25), 2) <= expected_val:
            coins[3] += 1
            change += 0.25
        elif round((change + 0.1), 2) <= expected_val:
            coins[2] += 1
            change += 0.1
        elif round((change + 0.05), 2) <= expected_val:
            coins[1] += 1
            change += 0.05
        elif round((change + 0.01), 2) <= expected_val:
            coins[0] += 1
            change += 0.01
    return coins


if __name__ == "__main__":
    print(f'my_result: ${get_change(5, 0.99)}')





