# String 3
namn = "kurt johan andersson"
L = len(namn)+1
 
j = 1
namn2 = (namn[0].upper())
 
for i in range(j,L):
    print(i)
    index = namn.find(' ',j,L)
    print(index)
    if index >= 0:
        namn2 = namn2 + (namn[j:index +1])
        namn2 = namn2 + (namn[index +1].upper())
        j = index + 2
        print(j)
    else:
        namn2 = namn2 + namn[j:L]
 
print(namn2)