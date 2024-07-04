from itertools import permutations


def solution(k, dungeons):
    answer = 0

    for tired in permutations(dungeons, len(dungeons)):
        potion = k
        dg = 0

        for need, spend in tired:
            if potion >= need:
                dg += 1
                potion -= spend
        answer = max(answer, dg)

    return answer
