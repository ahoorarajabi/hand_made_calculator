number1=float(input('adade aval ra vared konid: '))
operator=input("amal mored nazar +,-,*,/ ===>")
number2=float(input('adade dovom ra vared konid: '))
if operator == "+":
    print(f'{int(number1)}+{int(number2)}={number1+number2}')
elif operator == "-":
    print(f'{int(number1)}-{int(number2)}={number1-number2}')
elif operator == "*":
    print(f'{int(number1)}×{int(number2)}={number1*number2}')
elif operator == "/":
    print(f'{int(number1)}÷{int(number2)}={number1/number2}')