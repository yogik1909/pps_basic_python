a = [10, 0]
print(f"a: {a}")
print(f"id(a): {id(a)}")
b = a
print(f"b: {b}")
print(f"id(b): {id(b)}")
print("Выполнили операцию над переменной а, и снова выедем их значения и идентификаторы")
a.append(20)
a[1] = 30
print(f"a: {a}")
print(f"id(a): {id(a)}")
print(f"b: {b}")
print(f"id(b): {id(b)}")
