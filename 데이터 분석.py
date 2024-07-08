def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {"code":0, "date":1, "maximum":2, "remain":3}

    for i in data:
        # ext값이 val_ext보다 작은 데이터만 answer에 추가
        if i[dict[ext]] < val_ext:
            answer.append(i)

    answer.sort(key=lambda x:x[dict[sort_by]])

    return answer
