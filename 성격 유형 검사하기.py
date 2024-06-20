def solution(survey, choices):
    answer = ''
    point = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for s,c in zip(survey, choices):
        if c < 4:
            point[s[0]] += 4 - c
        elif c > 4:
            point[s[1]] += c - 4

    point_list = list(point.items())

    for i in range(0, 8, 2):
        if point_list[i][1] < point_list[i+1][1]:
            answer += point_list[i+1][0]
        else:
            answer += point_list[i][0]

    return answer

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
