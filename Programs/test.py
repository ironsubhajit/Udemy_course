def get_set_of_infected_player(initial_speed):
    #print(f"list: {initial_speed} length: {len(initial_speed)}")
    infected_player = []
    infected = []
    smallest_infected = 1
    greatest_infected = 1
    for i in range(0, len(initial_speed)):
        for j in range(i+1, len(initial_speed)):
            expr = ((initial_speed[i]+i) - (initial_speed[j]+j))
            #print(f"expr for i:{i} and j:{j}: {expr}")
            if expr == 0:
                infected.append(i)
                infected.append(j)
                #print(infected)
    set_infected = set(infected)
    if len(set_infected) == len(initial_speed):
        smallest_infected = len(initial_speed)
        greatest_infected = len(initial_speed)
    elif len(set_infected) < len(initial_speed):
        greatest_infected = len(set_infected)
    infected_player.append(smallest_infected)
    infected_player.append(greatest_infected)
    return f"{infected_player[0]} {infected_player[1]}"


t = int(input())
for i in range(t):
    n = int(input())
    initial_speed = list(map(int, input().split(sep=' ', maxsplit=n)))
    print(get_set_of_infected_player(initial_speed))
