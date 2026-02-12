l = [1, 2, 3, 4, 5]
print(f"l: {l}")
l[0:3] = [10, 20, 30]
print(f"l: {l}")
l[0:3] = "123"
print(f"l: {l}")
del l[0]
print(f"l: {l}")
del l[0:2]
print(f"l: {l}")
l.append(6)
print(f"l: {l}")
l.insert(0, 3)
print(f"l: {l}")
l[:1] = [1, 2, 3]
print(f"l: {l}")
l.remove(6)
print(f"l: {l}")
