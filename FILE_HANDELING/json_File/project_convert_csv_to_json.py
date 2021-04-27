import json

json_list = []

with open('csv_file.txt', 'r') as file:
    for line in file.readlines():
        club, city, country = line.strip().split(",")
        data = {
            "club": club,
            "city": city,
            "country": country
        }
        json_list.append(data)


with open('json_file.txt', 'w') as file:
    json.dump(json_list, file)
    print(f"{file.name} is now a converted json file.")
