def calculate(a, b, c):
    if c:
        print (a+b)
    else:
        print (a-b)

a = int(input("podaj a: "))
b = int(input("podaj b: "))
c = bool(int(input("Dodawanie, wpisz 1, odejmowanie wpisz 0: ")))
calculate(a ,b ,c)