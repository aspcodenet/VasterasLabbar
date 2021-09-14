# Gör ett program där användaren får mata in en mening t ex ”Detta är min text
#som jag matar in”. Programmet skall räkna ut hur många ord meningen består av
#och meddela användaren om detta.

s = "Detta är min text som jag matar in"
antalOrd = 1
for character in s:
    if character == " ":
        antalOrd = antalOrd + 1

#be användaren mata in en mailadress. Programmet skall kontrollera att inmatningen är
#rätt dvs att det finns ett @ tecken och att det finns en . med 2 eller 3 tecken efter.
#Meddela användaren om det är rätt eller felaktig adress

while True:
    email = input("Mata in en epostadress")
    index = email.find("@")
    indexOfDot = email.rfind(".")
    antalAfterDot = len(email) - indexOfDot - 1
    if index == -1 or indexOfDot == -1 or  antalAfterDot < 2 or antalAfterDot > 3:
        print("Invalid epostadress")
    else:
        break


# Du har en sträng med texten ”Detta är en sträng som du skall ändra”. Ersätt via kod
# alla blanktecken i strängen med tecknet * . Räkna sedan ut via kod hur många
# förekomster det finns av tecknet * i strängen.
s = "Detta är en sträng som du skall ändra"
s = s.replace(" ", "*")
antalStars = 0
for c in s:
    if c == "*":
        antalStars = antalStars + 1

print(antalStars)





str1 = "kurt stefan andersson"
str2 = str1.split()
for name in str2:
    print(name[0].upper()+name[1:], end=" ")



# Du har strängen string namn="kurt andersson";
# Skriv kod så att förnamn och efternamn i variabeln namn börjar med stora bokstäver.
# Resultatet skall bli så här "Kurt Andersson"

namn = "leif stefan holmberg" #Leif Stefan Holmberg
nyttNamn = ""
FirstLetter = True
LastLetterWasSpace = False

for bokstav in namn:
    if FirstLetter == True or LastLetterWasSpace == True:
        nyttNamn = nyttNamn + bokstav.upper()
    else:
        nyttNamn = nyttNamn + bokstav
    FirstLetter = False
    if bokstav == " ":
        LastLetterWasSpace = True
    else:
        LastLetterWasSpace = False



import random
s = "Hello world"
index = s.find("w")
print(index)

index = s.find("@")
if(index == -1):
    print("Det är ingen epostaddress")


while True:
    print("Rolling the dice")
    print("The values are")
    randomNumber1 = random.randint(1,6)
    randomNumber2 = random.randint(1,6)
    print(randomNumber1)
    print(randomNumber2)

    c = input("Roll the dice again?")

    if c != "y" and c != "yes":
        break


    # if  not (  c == "y" or c == "yes" ):
    #     break


    # if c == "y" or c == "yes":
    #     continue
    # else:
    #     break



start = int(input("Mata in tal 1"))
for i in range(start-1,0,-1):
    print(i)







summan = 0
for i in range(10):
    start = int(input("Mata in tal:"))
    summa = summa + start

    print(f"Summan av de inmatade talen är:{summa}")









start = int(input("Mata in tal 1"))
slut = int(input("Mata in tal 2"))

#for i in range(1919,1972):
for i in range(start+1,slut):
    print(i)

print("Slut")

while True:
    print("1. Starta spelet")
    print("2. Se highscore")
    print("3. Avsluta")
    selection = input()
    if selection == "3":
        break
    if selection == "2":
        print("Visa highscore")
        input("Press enter to go back to menu")
    if selection == "1":
        print("*** GAME STARTING ***")
        # koda spelet
        input("Press enter to go back to menu")



# for i in range(2022,1972,-4):
#     print(i)

# i = 1972
# while i >= 2022:
#     print( i)    
#     i = i + 4


# val = input("Ange kategori")
# while val != "Pensionär" and val != "Student":
#     print("Ange ett av valen Pensionär och Student")
#     val = input("Ange kategori")


while True:
    val = input("Ange kategori")
    if  val == "Pensionär":
        break
    if  val == "Student":
        break
    print("Ange ett av valen Pensionär och Student")

if val == "Pensionär":
    print("30 kr")
elif val == "Student":
    print("20 kr")


# while True:
#     print("Vill du fortsätta Skriv in J eller N")
#     i = input()
#     if i == "J":
#         print("Kör spelet")
#     elif i == "N":
#         print("Hej då")
#         break

# print("aaaa")


# print("Start")
# x=5
# while x > 0:
#     print(x)
#     x=x-1

# print("Klar")





# while True:
#     print("do this forever….")
#     if input("exit j/n?") == "j":
#         break