from time import sleep, time
from random import choice
import json
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

languages = {"en": "English", "ua": "Українська", "ru": "Русский"}
languagesList = ["en", "ua", "ru"]

final = ""
alfa = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "#", "*"]

y = 0
for x in languages:
    print(str(y) + " - " + languages[x])
    y += 1

print()

language = input("Choose your language: ")

language = languagesList[int(language)]


os.system("cls")


with open(current_dir+"/"+language+".json", "r", encoding="utf-8") as file:
    langDict = json.load(file)


print(langDict["start1"])
print()
print(langDict["start2"])
print()
print()
inp = input(langDict["input"])

if inp == "1":
    kolvo = input(langDict["inputNumberCharacters"]) #Пароль будет создан из рандомных символов 
    for y in range(int(kolvo)):
        final = final + choice(alfa)
elif inp == "2":
    final = input(langDict["inputYourPassword"])
else:
    print(langDict["Error"])
    quit()

ai = 0
fi=0
res = ""
popitok = 0

for j in range(100):
    print()

print(langDict["PasswordIs"] + final)
print()
sleep(1.5)
print(langDict["startSearch"])
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print(langDict["start"])
print()
print()


startT = time()
    
while 1:
    sleep(0.02)
    popitok += 1
    print(res+alfa[ai])
    if alfa[ai] == final[fi]:
        res = res + alfa[ai]
        ai = 0
        fi = fi+1
        if fi==len(final):
            finT = time()
            break
    else:
        ai = ai+1

timedT = int(finT-startT)
timedT2 = finT-startT - float(timedT)
timedT3 = round(timedT2, 3)
finalT = str(timedT) + str(timedT3)[1:]

if float(finalT) >= 60:
    timedS = float(finalT) // 60
    finalT = float(finalT) - 60*timedS
    finalT = round(finalT, int(finalT)+2)
    
    finalT = str(int(timedS)) + langDict("min") + str(finalT) + langDict("sec")
else:
    finalT = str(finalT) + langDict["sec"]

 
print()
print()
 
if res == final:
    print(langDict["succefulSearch"])
    print()
    print(final + langDict["InitialPassword"])
    print(res + langDict["SelectedPassword"])
 
    print()
    print()
 
    print(langDict["info"])
    print(langDict["selectionAttempts"]+str(popitok) + langDict["attemps"])
    print(langDict["selectionTime"] + finalT)


print()
print()
input(langDict["pressEnter"])
