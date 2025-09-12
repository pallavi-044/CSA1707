from collections import deque

def water_jug(x, y, z):
    queue = deque([(0, 0)])
    visited = set((0, 0))
    operations = []

    while queue:
        a, b = queue.popleft()
        if a == z or b == z:
            return operations + [(a, b)]

        # Fill jug x
        if a < x and (x, b) not in visited:
            queue.append((x, b))
            visited.add((x, b))
            operations.append(("Fill jug x", (x, b)))

        # Fill jug y
        if b < y and (a, y) not in visited:
            queue.append((a, y))
            visited.add((a, y))
            operations.append(("Fill jug y", (a, y)))

        # Empty jug x
        if a > 0 and (0, b) not in visited:
            queue.append((0, b))
            visited.add((0, b))
            operations.append(("Empty jug x", (0, b)))

        # Empty jug y
        if b > 0 and (a, 0) not in visited:
            queue.append((a, 0))
            visited.add((a, 0))
            operations.append(("Empty jug y", (a, 0)))

        # Pour from jug x to jug y
        pour_amount = min(a, y - b)
        if pour_amount > 0 and (a - pour_amount, b + pour_amount) not in visited:
            queue.append((a - pour_amount, b + pour_amount))
            visited.add((a - pour_amount, b + pour_amount))
            operations.append(("Pour from jug x to jug y", (a - pour_amount, b + pour_amount)))

        # Pour from jug y to jug x
        pour_amount = min(b, x - a)
        if pour_amount > 0 and (a + pour_amount, b - pour_amount) not in visited:
            queue.append((a + pour_amount, b - pour_amount))
            visited.add((a + pour_amount, b - pour_amount))
            operations.append(("Pour from jug y to jug x", (a + pour_amount, b - pour_amount)))

    return None

# Example usage
x = 3
y = 5
z = 4
result = water_jug(x, y, z)
if result:
    for operation, state in result:
        print(f"{operation}: {state}")
else:
    print("No solution found")
