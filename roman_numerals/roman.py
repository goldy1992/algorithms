class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        count = 0

        size = len(s)
        while count < size:
            current_val=s[count]

            if current_val == 'I':
                next_idx = count + 1
                if next_idx < size:
                    if s[next_idx] == 'V':
                        total += 4
                        count += 2
                    elif s[next_idx] == 'X':
                        total += 9
                        count += 2
                    else:
                        count += 1
                        total += 1
                else:
                    count += 1
                    total += 1
            elif current_val == 'V':
                count += 1
                total += 5
            elif current_val == 'X':
                next_idx = count + 1
                if next_idx < size:
                    if s[next_idx] == 'L':
                        total += 40
                        count += 2
                    elif s[next_idx] == 'C':
                        total += 90
                        count += 2
                    else:
                        count += 1
                        total += 10
                else:
                    count += 1
                    total += 10
            elif current_val == 'L':
                count += 1
                total += 50
            elif current_val == 'C':
                next_idx = count + 1
                if next_idx < size:
                    if s[next_idx] == 'D':
                        total += 400
                        count += 2
                    elif s[next_idx] == 'M':
                        total += 900
                        count += 2
                    else:
                        count += 1
                        total += 100
                else:
                    count += 1
                    total += 100
            elif current_val == 'D':
                total += 500
                count += 1
            elif current_val == 'M':
                total += 1000
                count += 1

        return total