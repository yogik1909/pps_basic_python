a = 10
print(f"a: {a}")
print(f"id(a): {id(a)}")
b = a
print(f"b: {b}")
print(f"id(b): {id(b)}")
print("Выполнили операцию над переменной а, и снова выедем их значения и идентификаторы")
a = 7
print(f"a: {a}")
print(f"id(a): {id(a)}")
print(b)
print(f"id(b): {id(b)}")
