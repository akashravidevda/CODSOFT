message =""" 
  0)  Exit
  1)  Add Contact:
  2)  View Contact List
  3)  Search Contact
  4)  Update Contact:
  5)  Delete Contact
"""
def add(contact):
			name = input("\nEnter name : ")
			num = input("Enter number : ")
			print("contact added !")
			contact[name] = num
			display(contact)
def  display(a):
	km = [i for i in a]
	print(min(km))
	print("Name :"," number  :".rjust(len(max(km)),"*")) 
	for i in a :
		if len(min(km)) > 4:
			print(i.rjust(len(min(km))),contact[i],sep = "    ")
		else :
			print(i,contact[i],sep="   ")
	
def  phonebook(contact):
	while 1:
		print(message)
		choice = (input("Please enter your operation number "))
		try:
		 if int(choice) == 1:
				add(contact)
		 elif int(choice) == 2:
			      display(contact)
#				print("Name:      contact :")
#				for i in contact:
#					print(i,contact[i])
		 elif int(choice) == 3:
				search = input("Enter the cintact name to be searched : ")
				if search in contact:
					print(search ,f"'s contact number is {contact[search]}")
				else :
					print("The contact doesn't exist. ")		
		 elif choice == 4:
			       up = input("Enter the contact namr to be updated : ")
			       if up in contact:
			       	newnum = input("Enter the new number to be updated : ")
			       	contact[up] = newnum
			       else :
			       	print("The enter contact does not exist : ")
		 elif choice == 5:
		 	rem = input("Enter the contact name to be deleted : ")
		 	if rem in contact :
		 		contact.pop(rem)
		 	else:
				 print("That contact doesn,t exist :  ")
		 elif choice == 0:
				break
		 else :
			  print("To exit the app please enter  0")
		except :
			print("please enter the serial number of the above mentioned operation")
contact = {"alek":983964575}
phonebook(contact)