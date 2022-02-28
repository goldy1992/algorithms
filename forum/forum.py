
def solution(message, K):
    length = len(message)
    if K >= length:
        return message

    crop_point = K-1

    while crop_point > 0:
        current_char = message[crop_point]
        if current_char == ' ':
            return message[:crop_point]
        elif (crop_point + 1) < length and message[crop_point + 1] == ' ':
            return message[:crop_point+1]
        else:
            crop_point -= 1

    return ''
