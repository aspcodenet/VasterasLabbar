namn = "leif stefan holmberg"

first = True
beforeWasSpace = False

nyNamn = ""
for x in namn:
    if first or beforeWasSpace:
        nyNamn = x.upper()
    else:
        nyNamn = nyNamn + x
    first = False
    beforeWasSpace = x == ' '


namn = "Stefan*ffsd*sfdffsd*sdadfsa"
antalStars = 0
for x in namn:
     if x == '*':
         antalStars = antalStars + 1




namn  = "Hwllo woeld"
index = namn.find("w")



# namn = "Stefan"
# index = namn.find("St")
# if index == -1:
#     print("Fanns inte")
# else:
#     print(f"Hittades på position {index}")    


while True:
    txt = input("Skriv text>:")
    index = txt.find("moron") 
    if index >= 0:
        print("Utvisning. Gå och tvätta munnen")
        break
    txt = txt.replace("idiot", "*****")
    txt = txt.replace("dumskalle", "*********")
    print(txt)


while True:
    forNamn = input("Förnamn")
    if len(forNamn) < 10:
        break
    print("Fel!!! för lång")

forNamnInLowerCase = forNamn.lower()

if forNamnInLowerCase == "stefan":
    print("Yes")


efterNamn = input("Efternamn")
fullName = forNamn + " " + efterNamn
print(fullName)



# namn = "Jag heter Stefan men kallas 'Steffe'"
# namn = 'Jag heter Stefan men kallas "Steffe"'
namn = "Stefan"
age = 49
#print("Du heter", namn, "och är", age, "år" )
txt = f"Du heter {namn} och är {age+10} år"
print(txt)



for i in range(10):
    tal = input(f"Ange tal nummer {i+1}")