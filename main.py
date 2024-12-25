import os, time

red = "\033[31m"
blue = "\033[34m"
yellow = "\33[33m"
green = "\033[32m"
magenta = "\033[35m"
default = "\033[0m"

listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)):
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)

def spamAll(max):
  for i in range(0, max):
    os.system("clear")
    time.sleep(1)
    print(f"""Email {i+1}

Dear {blue}{listOfEmail[i]}{default}

It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't, we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III""")
    time.sleep(2)
    os.system("clear")

while True:
  print(f"{red:>35}SPAMMER Inc.{default}")
  print()
  time.sleep(1)
  menu = input(f"1. {green}Add email\n{default}2: {red}Remove email\n{default}3. {yellow}Show emails\n{default}4. {magenta}Get SPAMMING\n{default}> ")
  if menu == "1":
    email = input("Email: ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email : ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  elif menu == "4":
    spamAll(2)
  os.system("clear")
