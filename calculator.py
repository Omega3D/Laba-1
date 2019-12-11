a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
action = input("Введіть дію: ")
result = None
if action=="+":
    result = a+b
elif action=="-":
    result = a-b
elif action == '*':
     result = a*b
elif action == '/':
    result = a/b

print(result)
