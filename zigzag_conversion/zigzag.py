class Solution:

    def convert(self, s: str, numRows: int) -> str:
        arr = []
        for i in range(0, numRows):
            arr.append([])

        count = 1
        row_num_for_mode_0 = 0
        for char in s:
            if count in (1, numRows):
                arr[row_num_for_mode_0].append(char)
                row_num_for_mode_0 += 1
                if row_num_for_mode_0 >= numRows:
                    row_num_for_mode_0 = 0
                    count += 1
                    if count >= numRows:
                        count = 1

            else:
                arr[numRows - count].append(char)
                count += 1
                if count >= numRows:
                    count = 1

        to_return = ""

        for a in arr:
            for char in a:
                to_return += char

        return to_return
