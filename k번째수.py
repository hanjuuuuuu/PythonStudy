def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        substring = array[commands[i][0]-1:commands[i][1]]
        substring.sort()
        num = substring[commands[i][2]-1]
        answer.append(num)

    return answer

solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]])
