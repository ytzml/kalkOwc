<<<<<<< HEAD
def dodaj():
    a = int(input())
    b = int(input())
    print(a+b)

def get_help():
    print('podaj dwie liczby a program je doda')

get_help()
dodaj()
=======
def dodaj(a, b):
    wynik = a + b
    return wynik
    
a = int(input())
b = int(input())
wynik = dodaj(a,b)
print(wynik)
>>>>>>> zmiana_funkcji_dodawania
