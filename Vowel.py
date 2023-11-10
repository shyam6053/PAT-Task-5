print("Please enter your sentence")
s="Guvi Geeks Private Limited"
A=E=I=O=U=V=0
for i in s:
    if i=="a":
        A=A+1
        V=V+1
    elif i=="A":
        A=A+1
        V=V+1
    elif i=="e":
        E=E+1
        V=V+1
    elif i=="E":
        E=E+1
        V=V+1
    elif i=="i":
        I=I+1
        V=V+1
    elif i=="I":
        I=I+1
        V=V+1
    elif i=="o":
        O=O+1
        V=V+1
    elif i=="O":
        O=O+1
        V=V+1
    elif i=="u":
        U=U+1
        V=V+1
    elif i=="U":
        U=U+1
        V=V+1
print("The number of Vowels is",V)
print("The number of a,e,i,o and u are",A,",",E,",",I, ",",O,"and",U,"respectively")