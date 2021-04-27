'''
def get_infected_player(initial_speed):
    number_of_player = len(initial_speed)
    infected = []

    for i in range(number_of_player):
        infect_for_each_i = [1]
        for j in range(number_of_player):
            velocity_diff = (initial_speed[i] - initial_speed[j])
            if velocity_diff != 0:
                index_diff = (j-i)
                time = (index_diff/velocity_diff)
                if time > 0:
                    infect_for_each_i.append(1)
        infected.append(sum(infect_for_each_i))
        #if len(infect_for_each_i) == number_of_player:
         #   return f"{number_of_player} {number_of_player}"

    infected.sort()
    infect_set = set(infected)
    if len(infect_set) > 1:
        max_infect = list(infect_set)[-1]
        min_infect = list(infect_set)[-2]
    elif len(infect_set) == 1:
        max_infect = list(infect_set)[-1]
        min_infect = max_infect
    else:
        min_infect = 1
        max_infect = 1
    
    return f"{min_infect} {max_infect}"


test_case = int(input())
for i in range(test_case):
    n = int(input())
    initial_speed = list(map(int, input().split(sep=' ', maxsplit=n)))
    print(get_infected_player(initial_speed))
'''


def swap_element(arr1, arr2):
    sum_arr1 = sum(arr1)
    sum_arr2 = sum(arr2)
    swap = 0
    for i in arr1:
        for j in arr2:
            new_sum_arr1 = sum_arr1 - i + j
            new_sum_arr2 = sum_arr2 - j + i
            if new_sum_arr1 == new_sum_arr2:
                swap += 1

    return swap


t = int(input("test case: "))
swap_no = 0
for i in range(t):
    n = int(input("no of n: "))
    arr = [x for x in range(1,n)]
    for m in range(1,n):
        arr1 = arr[m:]
        arr2 = arr[:m]
        swap_no += swap_element(arr1, arr2)
    print("total swap possible: ",swap_no)

