def large_count_sum(arr):

    sum = 0
    max = 0
    start = 0
    start_max = 0
    end = 0

    for i in range(len(arr)):

        if sum == 0:
            start = i
        sum = sum + arr[i]

        if sum > 0:
            if sum > max:
                end = i
                start_max = start
                max = sum

        else:
            sum = 0

    return start_max, end, max


print large_count_sum ([-3,3,-6])
