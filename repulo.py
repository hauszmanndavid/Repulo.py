import random

Llista = []

#A rész
for i in range(20):
    Llista.append(random.randint(0,9))

print("A mérési eredmények:", ' '.join(map(str,Llista)))

#B rész
print("Ez a legnagyobb hely: ", max(Llista))

#C rész