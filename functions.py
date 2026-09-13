'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword vs default arguments
(4) Scope
'''

print("===== Define (parametr) vs Call (argument) =====")
# built in function > print() type()
# FUNCTIONS - malum bir mantiqni ishga tushurub beruvchi kod block
# FUNCTIONS - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute - argument
result1 = greet("JOHN")
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)


print("===== Keyword & default arguments =====")

# DEFINE


def give_greet(name, age):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet("JOHN", 23)
print("result3:", result3)


print("===== Scope =====")

b = 100  # 3

# DEFINE


def calculate(a, b):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# CALL
calculate(5, 20)
