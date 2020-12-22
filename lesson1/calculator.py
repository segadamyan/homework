#calculator in polish notation
import os
import datetime
def check_num(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

def oper(exp):
	error = 0
	for i in range(1,len(exp)):
		if (exp[0].isnumeric() or not check_num(exp[i])):
			error = "Invalid expression"
	
	if (error ==0):
		result = float(exp[1])
		if (exp[0]=="+" or exp[0] == "add"):
			for i in range(2,len(exp)):
					result+=float(exp[i])
		elif (exp[0]=="-" or exp[0] == "sub"):
			for i in range(2,len(exp)):
				result-=float(exp[i])
		elif (exp[0]=="*" or exp[0] == "mul"):
			for i in range(2,len(exp)):
				result*=float(exp[i])
		elif (exp[0]=="/" or exp[0] == "div"):
			for i in range(2,len(exp)):
				if (exp[i] == "0"):
					error = "Divizion by zero"
					break
				result/=float(exp[i])
		else:
			error = "Invalid operation"
		date = datetime.datetime.now()
		if (error==0):
			if (result == int(result)):
				result = int(result)
			with open(os.path.join(os.getcwd(),"info.txt"),"a") as f:
				f.write(str(date))
				f.write(" :: INFO :: ")
				f.write(str(exp))
				f.write(" :: ")
				f.write(str(result))
				f.write("\n")
			print("Result: ",result)
			print("Report: INFO-",len(exp) -2, ", ERROR-0")
		else:
			with open(os.path.join(os.getcwd(),"error.txt"),"a") as f:
				f.write(str(date))
				f.write(" :: ERROR :: ")
				f.write(str(error))
				f.write(" :: ")
				f.write(str(exp))
				f.write("\n")
			print("Error: ",error)
			print("Report: INFO-",len(exp) -2, ", ERROR-1")
	else:
		date = datetime.datetime.now()
		with open(os.path.join(os.getcwd(),"error.txt"),"a") as f:
				f.write(str(date))
				f.write(" :: ERROR :: ")
				f.write(str(error))
				f.write(" :: ")
				f.write(str(exp))
				f.write("\n")
		print("Error: ",error)
		print("Report: INFO-",len(exp) -2, ", ERROR-1")

ex = input("Expression:")
space = list()
for i in range(0,len(ex)):
	if (ex[i] == " "):
		space.append(i)

exp = list()
if (not space[0]==0):
	exp.append(ex[:space[0]])

for i in range(0,len(space)-1):
	if (space[i]+1==space[i+1]):
		continue
	exp.append(ex[space[i]+1:space[i+1]])

if (not space[len(space)-1] == len(ex)-1):
	exp.append(ex[space[len(space)-1]+1:])

oper(exp)
	


