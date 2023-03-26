# Bold High Intensty
biblack="\33[1;90m"      # Black
bired="\33[1;91m"        # Red
bigreen="\33[1;92m"      # Green
biyellow="\33[1;93m"     # Yellow
biblue="\33[1;94m"       # Blue
bipurple="\33[1;95m"     # Purple
bicyan="\33[1;96m"       # Cyan
biehite="\33[1;97m"      # White
import os
while True:
	os.system("clear")
	print("""
    ╔════════════════════════════════════╗
    ║             SMS BOMBER                     ║
    ║     AUTHOR: MAMUNUL HASAN                  ║
    ║           VERSION : {version : 0.1}        ║
    ║            STATUS : FREE                   ║
    ╚════════════════════════════════════╝

""")

	print(bicyan+" [01] SMS BOOMBING [Unlimited Boombing Any Number]\n [02] CIRCLE BOOMBING [Unlimited Attack For Circle Number]\n")
	a=str(input(bipurple+" [>] Select Your Option : "))
	if a=="1":
		os.system("python3 XWarrior.py")
		a=input()
	elif a=="2":
		os.system("python3 XWarrior1.py")
		a=input()
	else:
		print("[x]Wrong Value Entered")
		a=input() 
		