

int 1, 2, 3
str "arefin ammur murgir bachchu"
float 1.2, 7.5
True, False

n = True
heart = 0
print(heart)


def add(num1, num2):
    result = num1 + num2
    return result


==, > , < , >= , <=


def sub(num1, num2):
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1
    return result


def mul(num1, num2):
    result = num1 * num2
    return result


def div(num1, num2):
    result = num1 / num2
    return result


1+2+3+4-5*9/1

n1 = 1
n2 = 2
sum = add(n1, n2)
print(f"add({n1},{n2}) = {sum}")
print(f"add({n1},{n2}) = {add(n1, n2)}")
print(f"{sum}")
n3 = 10
n4 = 2
diff = sub(n3, n4)
print(f"sub({n3},{n4}) = {diff}")

n5 = 1
n6 = 2
product = mul(n5, n6)
print(f"mul({n5},{n6}) = {product}")

n7 = 1
n8 = 2
divide = div(n7, n8)
print(f"div({n7},{n8}) = {divide}")

# -------------------------------------
# diff = sub(5, 10)
# print(diff)

# multi = mul(1, 2)
# print(multi)

# divide = div(1, 2)
# print(divide)
