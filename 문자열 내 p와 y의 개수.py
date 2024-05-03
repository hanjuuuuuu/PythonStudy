def solution(s):
    pCount = 0
    yCount = 0
    for i in s:
        if i == 'p' or i == 'P':
            pCount += 1
        if i == 'y' or i == 'Y':
            yCount += 1

    return True if pCount == yCount else False
