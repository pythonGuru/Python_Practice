def sum_partition(arr):

    d = {}

    s1 = []
    s2 = []

    s1_sum = 0
    l = len(arr)
    arr.sort()

    s1 = arr[0:l/2]
    for num in s1:
        s1_sum = s1_sum + num
        d[half] = s1_sum

    if s1_sum >= arr[l/2+1]:
        
    else:




    s2 = arr[l-1]



    for num in s2:
        s2_sum = s2_sum + num

    if s1_sum > s2_sum:
        abs_sum = s1_sum - s2_sum
    else:
        abs_sum = s2_sum - s1_sum

sum_partition([2,1,9,14,3])
