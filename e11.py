number1 = float(input("请输入一个数字："))
yunsuan = input("请输入一个运算符：")
number2 = float(input("请输入第二个数字："))
if yunsuan == "+":
    print (str(number1+number2))
elif yunsuan == "-":
    print(str(number1-number2))
elif yunsuan == "*":
    print(str(number1*number2))
elif yunsuan == "/":
    print(str(number1/number2))
else:print("输入有误")