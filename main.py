import random as ra
greetings = ["Hello!", "Hey!",  "GoodDay!"]
goodbyes = ["Bye!", "Later!",  "See you later!"]

print(ra.choice(greetings))
namec = input("Please input name here: ")
nr = open("name.txt",  "r")
nrr = nr.read()
if namec in nrr:
    print("Welcome " + namec)
    passwoc = input("Please enter password here: ")
    pr = open("pass.txt",  "r")
    prr = pr.read()
    if passwoc in prr:
        print(ra.choice(greetings))
        print("Would you like to add to your diary?")
        ans1 = input("Yes or No (y/n): ")
        if ans1 == "y":
            print("Alright!")
            addd = input("Type here (no enter key): ")
            di = open("diary.txt",  "a")
            di.write("\n" + addd)
            di.close()
            print("Added Succesfully")
        else:
            print("Would you like to read it")
            ans2 = input("Yes or No (y/n): ")
            if ans2 == "y":
                dia = open("diary.txt",  "r")
                diar = dia.readlines()
                print(diar)
            
    else:
        print("Wrong!")
else:
    print("Unauthorised User")
