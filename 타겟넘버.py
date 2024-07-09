def solution(numbers, target):
    answer = 0
    result = [0]
    # 리스트 순회하면서 업데이트 할 때는, 새로 생성
    for number in numbers:
        new = []
        for i in result:
            new.append(i + number)
            new.append(i - number)
        result = new
    for j in result:
        if j == target:
            answer += 1

    return answer
