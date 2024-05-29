"""
This is a simple password generator program where i have imported two modules random and and string. string to get charster elememts of password and 
random to pick random elements.
"""
import string as m
import random as r
password =[]		
	
#print(dir(m))
#print(m.ascii_letters)
#print(m.digits)

chr = m.ascii_letters
schr = m.punctuation
num = m.digits
try:
  length = int(input("Enter the lengh of paswword :"))
  if length< 4 :
  	print("The lenth must be atleast 4")
  elif length % 2 == 0:
       	for i in range(length // 2):
       		password.append(r.choice(chr))
       		password.append(r.choice(schr))
  else:
  		for i in range((length//2)-1):
  			password.append(r.choice(num))
  		for i in range((length // 2)):
  		   password.append(r.choice(chr))
  		   password.append(r.choice(schr))
  k = ""
  for i in password :
  	k += i
  print("password = ",k)
except :
    print("please enter numerical value only")  
