def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in range(len(cards1)-1):
        if goal.index(cards1[i]) > goal.index(cards1[i + 1]):
            answer = "No"
    for j in range(len(cards2)-1):
        if goal.index(cards2[j]) > goal.index(cards2[j + 1]):
            answer = "No"

    return answer

solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])