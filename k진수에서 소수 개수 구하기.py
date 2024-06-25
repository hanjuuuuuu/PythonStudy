import math


def solution(n, k):
    answer = 0

    # n을 k진수로 바꾸기
    k_num = ''
    while n > k - 1:
        k_num += str(n % k)
        n //= k
    k_num += str(n)
    k_num = ''.join(reversed(k_num))

    # 0을 기준으로 분할
    check_prime = k_num.split('0')

    # 소수 인지 확인
    for i in check_prime:
        if i == '':
            continue
        num = int(i)
        if num < 2:
            continue
        prime = True
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                prime = False
                break
        if prime:
            answer += 1

    return answer