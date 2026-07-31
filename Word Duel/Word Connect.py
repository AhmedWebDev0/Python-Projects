import termcolor
import pyfiglet

a = input("What's Player1 Name?\t")
while len(a) < 2:
    a = input("Please enter a valid Player1 name:\t")

h = input("What's Player2 Name?\t")
while len(h) < 2:
    h = input("Please enter a valid Player2 name:\t")
    
# print(dir(pyfiglet))
# print(dir(termcolor))
print(f"{termcolor.colored(pyfiglet.figlet_format(a), color = ("blue"))} {termcolor.colored(pyfiglet.figlet_format("VS"), color = ("blue"))} {termcolor.colored(pyfiglet.figlet_format(h), color = ("blue"))}")

score1 = 0
score2 = 0
mydict ={
    "a" : 15 ,
    "b" : 5 ,
    "c" : 8 ,
    "d" : 15 ,
    "e" : 13 ,
    "f" : 5 ,
    "g" : 5 ,
    "h" : 15 ,
    "i" : 12 ,
    "j" : 10 ,
}

print(f"Your chars Is :\n" + "#" * 21)
for key , value in mydict.items() :
    for y in key :
        print(f"#{y}" ,end = "")
print("#" +"\n"+ "#" * 21)

f = input(f"Player 1 _{a}_ :\t")
while len(f) < 2 or len(f) > 10 :
    f = input("Please enter the word for the first player:\t")

d = input(f"Player 2 _{h}_ :\t")
while len(d) < 2 or len(d) > 10 :
    d = input("Please enter the word for the second player:\t")

i = 0
for nam in f, d :
    if f[i] in key and d[i] in key :
        score1 += mydict[f[i]]
        score1 += mydict[d[i]]
        i += 1

if score1 < score2 :
    print(f"{termcolor.colored(pyfiglet.figlet_format(a) , color =("blue"))} {termcolor.colored(pyfiglet.figlet_format("Is Win!") , color =("blue"))}")

elif score1 > score2 :
    print(f"{termcolor.colored(pyfiglet.figlet_format(h) , color =("blue"))} {termcolor.colored(pyfiglet.figlet_format("Is Win!") , color =("blue"))}")

elif score1 == score2 :
    print(f"{termcolor.colored(pyfiglet.figlet_format(a) , color =("blue"))} {termcolor.colored(pyfiglet.figlet_format("&") , color =("blue"))} {termcolor.colored(pyfiglet.figlet_format(h) , color =("blue"))} {termcolor.colored(pyfiglet.figlet_format("Are Tied!") , color =("blue"))}")
