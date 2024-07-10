def solution(k, tangerine):
    answer = 0
    graph = []
    n = 0
    for i in range(len(tangerine)):
        if [tangerine[i], tangerine.count(tangerine[i])] not in graph:
            graph.append([tangerine[i], tangerine.count(tangerine[i])])
    graph.sort(key=lambda x: -x[1])

    for j in range(len(graph)):
        if n >= k:
            answer += j
            break
        else:
            n += graph[j][1]

    return answer
