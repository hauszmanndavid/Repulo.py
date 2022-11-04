import random

Llista = []

#A rész
for i in range(20):
    Llista.append(random.randint(0,9))

print("A mérési eredmények:", ' '.join(map(str,Llista)))

#B rész
print("Ez a legnagyobb hely: ", max(Llista))

#C rész

#D rész
viz = 0
for i in Llista:
    if i == 0:
        viz += 1

szárazfold = 20 - viz

if szárazfold > 10:
    print("A szárazföld több")
elif viz > 10:
    print("A víz több")
else:
    print("Mind a kettőből ugyanannyi van")