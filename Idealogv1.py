import time
import glob
print(time.strftime("%c"))
##FUNCTIONS!
def help():
	print("These are the show of commands to operate in this programmette:\nstart --> (new -> /quit, add -> /quit) \nread -->(/list, /quit) \nquit \n")
	
	
def new(name):
	idea = open(name +".txt",'w')
	idea.write(time.strftime("%c") + "\n\n")
	
	x = True
	
	while(x):
		a = str(input("Let's write now!\n") + '\n')
		if('/quit' in a):
			break
		else:
			idea.write(a)
	idea.close()
	
def add(name):
	idea = open(name + ".txt", 'r')
	print(idea.read())
	idea = open(name + ".txt", 'a')
	print(idea.write(time.strftime("%c\n\n" )))
	x = True
	while(x):
		a = str(input("Go on continue this idea!\n") + '\n')
		if("/quit" in a):
			break
		else:
			idea.write(a)
	idea.close()
def read():
	x = True
	while(x):
		a = input("type in the name of the file (Type '/list' to list, '/quit')\n")
		if('/quit' in a):
			break
		if('/list' in a):
			for filename in glob.glob('*.txt'):
				print(filename)
	
		else:
			idea = open(a + ".txt", 'r')
			print(idea.read())
			idea.close()
		
##MAIN PART!		
x = True
while(x):
	
	girdi = str(input("Welcome to the idea log! (type help for commands!)\n"))
	if(girdi== "help"):
		print(help())
	elif(girdi == "start"):
		dongu = input("Would you like to start a new idea or add to an existing idea?\n")
		if(dongu == "new"):
			a = str(input("enter the filename\n"))
			new(a)
		elif(dongu == "add"):
			add(input("Enter the filename\n"))
	elif(girdi == "read"):
		read()
	elif(girdi == "quit"):
		x = False
	