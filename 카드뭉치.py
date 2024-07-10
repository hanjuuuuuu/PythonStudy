from collections import deque


def solution(cards1, cards2, goal):
    answer = 'Yes'
    g = deque(goal)
    c1 = deque(cards1)
    c2 = deque(cards2)
    one, two = c1.popleft(), c2.popleft()
    print('here', one, two)

    while g:
        g1 = g.popleft()
        if g1 == one:
            if len(c1) > 0:
                one = c1.popleft()
        elif g1 == two:
            if len(c2) > 0:
                two = c2.popleft()
        else:
            answer = 'No'

    return answer


solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"])
