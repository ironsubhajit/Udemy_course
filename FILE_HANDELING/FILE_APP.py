friends_name_list = input("\nEnter your friends name(separated by commas,plz not use any space): ").split(",")

people = open('people_nearby.txt', 'r')
people_nearby_list = [line.strip() for line in people.readlines()]
people.close()

people_nearby_set = set(people_nearby_list)
friends_name_set = set(friends_name_list)
friends_nearby_set = friends_name_set.intersection(people_nearby_set)

my_friends = open('friend_name.txt', 'w')
for friend in friends_nearby_set:
    print("\n{} is near to you,meet and say hi!".format(friend))
    my_friends.write(f"{friend}\n")
my_friends.close()

