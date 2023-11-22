def calcule(num1, operator, num2):
    op = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
        }
    if operator in op:
        return op[operator](num1,num2)
        
print(calcule(5,"+",5))
print(calcule(10,"*",2))
print(calcule(100,"/",1))
print(calcule(5,"%",15))
print(calcule(8,"-",8))