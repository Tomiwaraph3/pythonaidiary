import random as ra
greetings = ["Hello!", "Hey!",  "GoodDay!"]
goodbyes = ["Bye!", "Later!",  "See you later!"]

print(ra.choice(greetings))
print("Input your name for configuration purposes")
name = input("Name: ")
n = open("name.txt",  "r")
nw = open("name.txt",  "w")
nw.write(name)
nw.close()
n.close()
print("Input your password for configuration purposes")
passwo = input("Password: ")
p = open("pass.txt", "r")
pw = open("pass.txt",  "w")
pw.write(passwo)
p.close()
pw.close()
print("Please delete this file after usage!")
