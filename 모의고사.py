def solution(answers):
    answer = []
    point = [0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            point[0] += 1
        if answers[i] == two[i % len(two)]:
            point[1] += 1
        if answers[i] == three[i % len(three)]:
            point[2] += 1

    for j in range(len(point)):
        if point[j] == max(point):
            answer.append(j+1)
    print(answer)
    return answer

