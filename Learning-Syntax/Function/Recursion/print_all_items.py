cities = ["New York", "Dhangadhi", "Kathmandu", "Pokhara", "Tokyo", "London", "Sydney", "Delhi"]
cities.sort()

def print_items(items, index = 0):
    if index >= len(items):
        return
    print(items[index])
    print_items(items, index + 1)

print_items(cities)