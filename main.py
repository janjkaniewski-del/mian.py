import math
PI = math.pi
print(PI)

print ("pole prostokata")
a = float(input("Podaj dlugosc boku a: "))
b = float(input("Podaj dlugosc boku b:"))
print ("licze pp prostokata")
print ("pole prostokata wynosi: ", a*b)

print("pole kwadratu")
c = float(input("Podaj dlugosc boku c: "))
print ("licze pp kwadratu")
print ("pole kwadratu wynosi: ", c**2)


print ("pole trapezu")
d= float(input("Podaj dlugosc boku d: "))
e = float(input("Podaj dlugosc boku e: "))
f = float(input("Podaj wysokosc trapezu f: "))
print ("licze pp trapezu")
print ("pole trapezu wynosi: ", (d+e)*f/2)

print ("pole trojkata")
g = float(input("Podaj dlugosc podstawy g:"))
h = float(input("Podaj wysokosc trojkata h :"))
print ("licze pp trojkata")
print ("pole trojkata wynosi: ", g*h/2)


print ("pole kola")
i = float(input("Podaj dlugosc promienia i:"))
print ("licze pp kola")
print ("pole kola wynosi: ", PI*i**2)


