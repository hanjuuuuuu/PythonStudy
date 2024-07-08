def solution(s):
    answer = []
    one, another = 0, 0
    x = s[0]
    for i in range(len(s)):
        if s[i] == x:
            one += 1
        elif s[i] != x:
            another += 1
        if one == another:
            answer.append(s[i])
            one, another = 0, 0
            if i != len(s)-1:
                x = s[i + 1]
        else:
            if i == len(s)-1:
                answer.append(s[i])

    return len(answer)


solution("abracadabra")
