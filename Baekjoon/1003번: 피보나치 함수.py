def get_result(N):
    if N == 0:
        return 1, 0
    elif N == 1:
        return 0, 1
    zero_count = [i for i in range(N + 1)]
    one_count = [i for i in range(N + 1)]
    zero_count[0] = 1
    one_count[0] = 0
    zero_count[1] = 0
    one_count[1] = 1
    zero_count[2] = 1
    one_count[2] = 1
    for index in range(3, N + 1):
        zero_count[index] = zero_count[index - 1] + zero_count[index - 2]
        one_count[index] = one_count[index - 1] + one_count[index - 2]

    return zero_count[N], one_count[N]


T = int(input())
for i in range(T):
    N = int(input())
    zero, one = get_result(N)
    print(zero, one)