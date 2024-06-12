"""'
This is a simple calculator program with very basic operation  
"""
print('''   This is a simple calculator -_-   ''')
op = ["+","-","/","*"]
try :
  a =int(input("\nEnter your first number : "))
  b = int(input("\nEnter your second number : "))
  print(f"Currently you can only chose from {op[0:]}")
  c = input(" Now chose the operation that must be conducted ")
  if c in op:
    if c == op[0]:
    	print("Result :  ",a+b)
    elif c == op[1]:
    	print("Result : ",a-b)
    elif c == op[2]:
    	print("Result : ",a/b)
    elif c == op[3]:
    	print("Result : ",a*b)
  else:
   	print("please pick the operator from the above only .")
except:
  	print("Please aenter numeric value only")



	