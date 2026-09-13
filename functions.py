'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword vs default arguments
(4) Scope
'''

print("===== Define vs Call =====")
# built in function > print() type()
# FUNCTIONS - malum bir mantiqni ishga tushurub beruvchi kod block
# FUNCTIONS - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute
result1 = greet("JOHN")
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)
