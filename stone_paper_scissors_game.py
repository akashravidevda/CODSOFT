"""
This is a simple program model of clasic game stone paper scissor . Here i have used random module to give the computer the feature of chosing different option after every turn
"""
import random as rd
#print(dir(rd))
a = ["Stone", "Paper","Scissor"]
player = 0
comp = 0
print("welcome player in this classic Stone Paper Scissor game : \n ")
print("Enter your choice from Stone ,Paper, Scissor when you see -> \n Note : your spelling and case must match as given above. \n")
for i in range(5):
	m = rd.choice(a)
	k = input("input ->  ")
	print(k," x ",m)
	if k == m:
		print("Draw")
	elif k =="Stone" and m == "Paper" :
		print(" stone is warapped by the paper")
		comp += 1
	elif k =="Stone" and m == "Scissor" :
		print(" stone has smahed the Scissor")
		player += 1
	elif k =="Scissor" and m == "Paper" :
		print(" Scissor have cut the Paper in two halfs")
		player += 1
	elif k =="Paper" and m == "Stone" :
		print(" Paper has warapped the Stone")
		player += 1	
	elif m =="Stone" and k == "Scissor" :
		print(" Scissor is crushed by the Stone")
		comp += 1
	elif m =="Scissor" and k == "Paper" :
		print(" Paper is been cut into two halfs")
		comp += 1
	else:
	    print("Wrong input ")
     
		
if comp < player :
	print(f"\n \t player you have won this round with {player} points") 		
elif comp > player :
	print(f"\n \tComputer  has won this round with {comp} points") 
else:
 	print("\n\tTie")

#print(rd.choice(a))