def find_in(iterable, finder, expected):
    count = 1
    for name in iterable:
        if finder(name) == expected:
            print(f"Found Name at {count}th position")
            return name
        count += 1
    raise NotFoundError(f"{expected} not found in provided iterable.")


class NotFoundError(Exception):
    pass


if __name__ == "__main__":
    print(find_in(['rolf', 'jose', 'jen'], lambda x: x, input("Enter Name: ")))

