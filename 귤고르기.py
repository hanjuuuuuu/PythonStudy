from collections import Counter


def solution(k, tangerine):
    # 귤 크기와 그 개수를 세기
    count_map = Counter(tangerine)

    # 귤 크기를 개수 기준으로 내림차순 정렬
    sorted_counts = sorted(count_map.values(), reverse=True)

    # k개를 선택하면서 종류 수를 최소화
    total = 0
    distinct_types = 0

    for count in sorted_counts:
        total += count
        distinct_types += 1
        if total >= k:
            break

    return distinct_types