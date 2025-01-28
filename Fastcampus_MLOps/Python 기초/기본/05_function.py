def welcome(city, name="Guest", room=[]) :
    room.append(101)
    print(f"Welcome to {city}! {name}, your can use room number is {room}.")

welcome("New York")
welcome("London", "John")
welcome(room=[202], name="Alice", city="Tokyo")

def welcome(city, name="Guest", room=None) :
    if room is None:
        room = []
    room.append(101)
    print(f"Welcome to {city}! {name}, your can use room number is {room}.")

welcome("New York")
welcome("London", "John")
welcome(room=[202], name="Alice", city="Tokyo")

def sum(*args) :
    total = 0
    for num in args:
        total += num
    return total
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age=26, city="New York")
info = {"name": "Tom", "age": 26, "city": "New York"}
print_info(**info)