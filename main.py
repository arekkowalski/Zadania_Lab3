from random import randint

# # Zad1
# a = [ 1 - x for x in  range(1, 11)]
# print(a)
#
# b = [ 4**y for y in range(8)]
# print(b)
#
# c = [x for x in b if x % 2 == 0]
# print(c)

# # Zad2
# randList = [randint(0, 100) for x in range(10)]
# randList.sort()
# print(randList)
#
# randEven = [x for x in randList if x%2==0]
# print(randEven)

# # Zad3
# produkty = {"banany":"Kg", "woda":"sztuka","ketchup":"sztuka","szynka":"Kg"}
# print(produkty)
#
# lista = [produkt for produkt in produkty if produkty.get(produkt) =="sztuka"]
# print(lista)

# # Zad4
# def czy_prostokatny(a, b, c):
#             a = float(a)
#             b = float(b)
#             c = float(c)
#             if (a<=0)|(b<=0)|(c<=0):
#                 return "Podano bledne wartości"
#             elif (a > b) & (a > c):
#                 check = b**2 + c**2
#                 if a**2 == check:
#                     return "Trojkat jest prostokatny"
#                 else:
#                     return "Trojkat nie jest prostokatny"
#             elif (b > a) & (b > c):
#                 check = a**2 + c**2
#                 if b**2 == check:
#                     return "Trojkat jest prostokatny"
#                 else:
#                     return "Trojkat nie jest prostokatny"
#             else :
#                 check = b ** 2 + a ** 2
#                 if c ** 2 == check:
#                     return "Trojkat jest prostokatny"
#                 else:
#                     return "Trojkat nie jest prostokatny"
#
# a = input("Podaj długość pierwszego boku trójkąta: ")
# b = input("Podaj długość drugiego boku trójkąta: ")
# c = input("Podaj długość trzeciego boku trójkąta: ")
# print(czy_prostokatny(a, b, c))

# # Zad5
# def pole_trapezu(a=1, b=1, h=1):
#         a = float(a)
#         b = float(b)
#         h = float(h)
#         if (a<=0)|(b<=0)|(h<=0):
#             return "Podano bledne wartosci"
#         else:
#             P = (a+b)*h/2
#             return P
# print(pole_trapezu())
#
# a = input("Podaj dlugosc pierwszej podstawy trapezu: ")
# b = input("Podaj dlugosc drugiej podstawy trapezu: ")
# h = input("Podaj wysokosc trapezu: ")
# print(pole_trapezu(a, b, h))

# Zad8
# def zakupy(**koszyk):
#     przedmioty = len(koszyk)
#     if przedmioty != 0:
#         suma = 0
#         ceny = [cena for cena in koszyk.values() if isinstance(cena, float) == True or isinstance(cena, int) == True]
#         print(ceny)
#         for x in range (len(ceny)):
#             suma+=float(ceny[x])
#     else:
#         return "Brak zakupów"
#     return suma
# print(zakupy(woda = 1, batonik = 2,mieso = 23.50))