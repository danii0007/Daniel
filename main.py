
import random

print("================================")
print("       LOJA GEJE NUMRIN")
print("================================")
print("Kam zgjedhur nje numer nga 1 deri ne 100.")

numri_sekret = random.randint(1, 100)
tentativat = 0

while True:
    pergjigjja = int(input("Shkruaj nje numer: "))
    tentativat += 1

    if pergjigjja < numri_sekret:
        print("Numri eshte me i madh! Provo perseri.")

    elif pergjigjja > numri_sekret:
        print("Numri eshte me i vogel! Provo perseri.")

    else:
        print("URIME! E gjete numrin!")
        print("Numri ishte:", numri_sekret)
        print("Tentativa:", tentativat)
        break

print("Faleminderit qe luajte!")
