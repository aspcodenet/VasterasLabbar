allaTal = [1,4,2,4]





allaSpelare = []
while True:
    print("1. Skapa ny spelare")
    print("2. Lista alla spelare")
    print("3. Skriv ut den som är först i listan")
    print("5. Hur många spelare finns det?")
    print("4. Avsluta")

    sel = input("Vad vill du göra:")
    if sel == "4":
        break
    if sel == "5":
        #Nu är det X spelare i listan
        #antal = len(allaSpelare)
        print(f"Nu är det {len(allaSpelare)} spelare i listan")
        #print(len(allaSpelare))
    break
    if sel == "3":
        print("***Den första är ***")
        print(allaSpelare[0])
    if sel == "1":
        print("***Ny spelare***")
        namn = input("Ange spelaren namn:")
        allaSpelare.append(namn)
    if sel == "2":
        print("*** Här är alla spelare***")
        for playerNamn in allaSpelare:
            print(playerNamn)            








minaBarn = ["Fanny", "Josefine", "Oliver", "2342"]
for namn in minaBarn:
    print(namn)

# Med en for-loop 
#  ta fram det största talet i denna lista
# och skriv ut

largestSoFar = 0
listaMedTal = [3,5555,222,9,1]     

for tal in listaMedTal:
    if tal > largestSoFar:
        largestSoFar = tal

print(largestSoFar)





