# Problem - https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

total_test_case = int(input())
for test_case in range(1, total_test_case+1):
    total_points = int(input())
    chk_points = input().split(' ')
    
    prev2 = prev1 = None
    count = 0
    for chk_point in chk_points:
        
        chk_point = int(chk_point)
        if not prev1:
            prev1 = chk_point
            continue
        
        if not prev2:
            prev2 = chk_point
            continue

        if prev2 > prev1 and  prev2 > chk_point:
            count += 1
        
        prev1 = prev2
        prev2 = chk_point

    print("Case #{}: {}".format(test_case, count))
        
