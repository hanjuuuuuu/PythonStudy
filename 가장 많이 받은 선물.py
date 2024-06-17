def solution(friends, gifts):
    answer = 0

    gift_map = {}
    giver_map = {}
    receiver_map = {}
    answer_map = {}

    # 선물을 주고받은 기록이 있다면 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.

    # 선물을 주고받은 기록이 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 작은 사람에게 선물을 하나 받습니다.
    # 선물 지수 = 자신이 친구들에게 준 선물의 수 - 받은 선물의 수

    for first in friends:
        inner_gift_map = {}
        for second in friends:
            if first == second:
                continue
            inner_gift_map[second] = 0
        gift_map[first] = inner_gift_map
        answer_map[first] = 0
        giver_map[first] = 0
        receiver_map[first] = 0

    for gift in gifts:
        giver, receiver = gift.split()
        gift_map[giver][receiver] += 1
        giver_map[giver] += 1
        receiver_map[receiver] += 1

    for i in range(len(friends) - 1):
        for j in range(i+1, len(friends)):
            a = friends[i]
            b = friends[j]

            a_count = gift_map[a][b]
            b_count = gift_map[b][a]

            if a_count > b_count:
                answer_map[a] += 1
            elif b_count > a_count:
                answer_map[b] += 1
            else:
                a_value = giver_map[a] - receiver_map[a]
                b_value = giver_map[b] - receiver_map[b]

                if a_value > b_value:
                    answer_map[a] += 1
                elif b_value > a_value:
                    answer_map[b] += 1

    return max(answer_map.values())


print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
