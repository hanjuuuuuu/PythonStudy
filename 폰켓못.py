def solution(nums):
    l = len(nums) // 2
    num = set(nums)

    if len(num) >= l:
        return l
    else:
        return len(num)
