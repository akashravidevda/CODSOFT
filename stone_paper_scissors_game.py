"""
This is a simple program model of clasic game stone paper scissor . Here i have used random module to give the computer the feature of chosing different option after every turn
"""
import random as rd
#print(dir(rd))
a = ["Stone", "Paper","Scissor"]
player = 0
comp = 0
print("welcome player in this classic Stone Paper Scissor game : \n ")
print("Enter your choice from Stone , Paper, Scissor when you see -> \n Note : your spelling and case must match as given above. \n")
while 1 :
	for i in range(5):
		m = rd.choice(a)
		k = input("input ->  ")
		if k == m:
			print("Draw")
			print(k," x ",m)
		elif k =="Stone" and m == "Paper" :
				print(" stone is warapped by the paper")
				print(k," x ",m)
				comp += 1
		elif k =="Stone" and m == "Scissor" :
			print(" stone has smahed the Scissor")
			print(k," x ",m)
			player += 1
		elif k =="Scissor" and m == "Paper" :
			print(" Scissor have cut the Paper in two halfs")
			print(k," x ",m)
			player += 1
		elif k =="Paper" and m == "Stone" :
			print(" Paper has warapped the Stone")
			print(k," x ",m)
			player += 1	
		elif m =="Stone" and k == "Scissor" :
			print(" Scissor is crushed by the Stone")
			print(k," x ",m)
			comp += 1
		elif m =="Scissor" and k == "Paper" :
			print(" Paper is been cut into two halfs")
			print(k," x ",m)
			comp += 1
		else:
			  print("Wrong input ")
	choice = input("Do you wanna have another round : Reply by Y as yes and N as no") 
	if choice == "N" or "n":
		   break
	else:
	    pass
     
		
if comp < player :
	print(f"\n \t player you have won this round with {player} points") 		
elif comp > player :
	print(f"\n \tComputer  has won this round with {comp} points") 
else:
 	print("\n\tTie")

#print(rd.choice(a))
