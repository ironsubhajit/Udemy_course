import csv


def write_to_file(output):
    with open("file.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows([elem.values() for elem in output]) #[["elem","elem"],nxtRow["elem","elem"],nxtRow...]


def read_from_file():
    with open("file.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']}\tDegree: {line['degree']}")


read_from_file()
