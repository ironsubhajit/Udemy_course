import json

# json.load function
file = open('friends_json.txt', 'r')
file_content = json.load(file)  # reads file & truns into a dict
file.close()

print(f"{file_content['friends'][0]}")

# json.dump function

cars = [
    {'make': 'ford', 'model': 'fiesta'},
    {'make': 'ford', 'model': 'focus'}
]

file1 = open('cars_jason.txt', 'w')
json.dump(cars, file1)
file1.close()
print(f"{file.name} created successfully!")

# json.loads for loading an json string into a dict

cars = '[{"name": "ford", "release": 1980}]'
correct = json.loads(cars)
print(f"{correct[0]['name']}")
