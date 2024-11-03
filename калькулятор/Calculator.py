
what = input("что делаем? | what to do?(+, -, *, /, //, %, **)")
a = float(input("введи первое число | enter the first number:"))
b = float(input("введи второе число | enter the second number:"))


if what =="+":
    c = a + b
    print("ответ | answer:" + str(c))
elif what == "-":
    c = a - b
    print("ответ | answer:" + str(c))
elif what == "*":
    c = a * b
    print("ответ | answer:" + str(c))
elif what == "/":
    c = a / b
    print("ответ | answer:" + str(c)) 
elif what == "//":
    c = a // b
    print("ответ | answer:" + str(c))
elif what == "%":
    c = a % b
    print("ответ | answer:" + str(c))
elif what == "**":
    c = a ** b
    print("ответ | answer:" + str(c))
else:
    print("что то не так... | Something's wrong...")

input()
