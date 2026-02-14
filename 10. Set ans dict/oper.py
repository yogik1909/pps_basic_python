a = {1, 2, 3}
b = {3, 4, 5}

print("Объединение:")
print(f"Выражение( a | b): {a | b}")
print(a.union(b))

print("Пересечение:")
print(a & b)
print(a.intersection(b))

print("Разность:")
print(f"Выражение( a - b): {a - b}")
print(a.difference(b))

print(f"Выражение( b - a): {b - a}")
print(b.difference(a))

print("Симметрическая разность:")
print(f"Выражение( a ^ b): {a ^ b}")
print(a.symmetric_difference(b))

print(f"Выражение( b ^ a): {b ^ a}")
print(b.symmetric_difference(a))

print("Дискретное множество:")
print(f"Выражение( a < b): {a < b}")
print(a.issubset(b))

print(f"Выражение( b < a): {b < a}")
print(b.issubset(a))
