def add(*args):
    return sum(args)

print("Результат сложения множества чисел:", add(5, 10, 15, 20))

def print_info(name, *args, **kwargs):
    print(f"Name: {name}")
    print("Args:", args)
    print("Kwargs:", kwargs)

print_info("Alice", 1, 2, 3, age=25, city="New York")