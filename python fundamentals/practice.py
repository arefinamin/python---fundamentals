import math
memory_location = 1
print(memory_location)


course = "StringsTutorial"
print(len(course))
print(course[-1])
print(course[:3])

lesson = "Escape \\Sequences"

print(lesson)


initial = "a"
final = "b"
full = f"{len(initial)} {len(final)}"
print(full)

lesson = " string methods "
print(lesson.upper())
print(lesson.lower())
print(lesson.lstrip())
print(lesson.rstrip())
print(lesson.find("pro"))
print(lesson.replace("t", "s"))
print("tri" in lesson)
print("pro" not in lesson)

print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)
print(10**3)

# x = x + 3
# x += 3

print(round(4.5))
print(abs(-4.1))

print(math.ceil(4.1))

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
# print(type(x))
# y = x + 1
# int(x)
# float(x)
# bool(x)
# str(x)
10 > 3
