#calculator in polish notation
import os
import datetime
operations ={'+','-','*','/','add','sub','mul','div'}
def isOper(num) -> bool:
    for i in operations:
        if num == i:
            return True
    else :
        return False
def isNum(num) -> bool:
	try:
		float(num)
		return True
	except ValueError:
		return False
opCount = 0
def isCor(exp) -> bool:
    if len(exp) < 3:
        return False
    if isNum(exp[len(exp)-3]) or isOper(exp[len(exp)-2]) or isOper(exp[len(exp)-1]):
        return False
    for i in exp:
        if not isOper(i) and not isNum(i):
            return False
        elif isOper(i):
            global opCount
            opCount += 1
    else :
        return True
    
def oper(op1,num1,num2):
    if op1 == '+' or op1 == 'add':
        return float(num1) + float(num2)
    elif op1 == '-' or op1 == 'sub':
        return float(num1) - float(num2)
    elif op1 == '*' or op1 == 'mul':
        return float(num1) * float(num2)
    elif op1 == '/' or op1 == 'div':
        if (not str(num2) == '0'):
            return float(num1) / float(num2)
        else :
            print("Error: Zero Division")
            print("Report: INFO-",opCount, ", ERROR-1")
            date = datetime.datetime.now()
            with open(os.path.join(os.getcwd(),"error.txt"),"a") as f:
                text = f'{str(date)} :: ERROR :: Zero Division  :: {ex} \n'
                f.write(text)
            exit()
    
ex = input("Expression:")
ex = ex.split()
if (isCor(ex)):
    for i in range(len(ex)-1,-1,-1):
        if (isOper(ex[i]) and isNum(ex[i+1]) and isNum(ex[i+2])):
            op = oper(ex[i],ex[i+1],ex[i+2])
        elif (isOper(ex[i]) and isNum(ex[i+1]) and isOper(ex[i+2])):
            op = oper(ex[i],ex[i+1],op)
        elif (isOper(ex[i]) and isOper(ex[i+1])):
            op = oper(ex[i],oper(ex[i+1],ex[i+2],ex[i+3]),op)
    if (op == int(op)):
        op = int(op)   
    print("Result: ", op)
    print("Report: INFO-",opCount, ", ERROR-0")
    date = datetime.datetime.now()
    with open(os.path.join(os.getcwd(),"info.txt"),"a") as f:
        text = f'{str(date)} :: INFO :: {ex}  :: {op} \n'
        f.write(text) 
else :
    print("Error: Invalid expression")
    print("Report: INFO-",opCount, ", ERROR-1")
    date = datetime.datetime.now()
    with open(os.path.join(os.getcwd(),"error.txt"),"a") as f:
        text = f'{str(date)} :: ERROR :: Invalid expression  :: {ex} \n'
        f.write(text)