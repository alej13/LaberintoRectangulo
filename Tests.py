from PruevaSeleccion.Laberinto import Laberinto

test1 = Laberinto(5, 9, [(2, 1), (2, 5), (3, 5), (4, 2), (4, 8), (5, 2), (5, 8)])
test2 = Laberinto(5, 9, [(2,1), (2,5), (2,8), (3,5),(4,2),(4,8),(5,2),(5,8)])
test3 = Laberinto(3, 3)
test4 = Laberinto(10,10, [(2,2),(2,7),(3,2),(6,2),(7,2),(7,6),(8,7)])
tests = [test1, test2, test3, test4]

for i in range(4):
    print(" Test " +str(i + 1))
    print(tests[i])
    if tests[i].evaluar_caminos() == -1:
        print("El laberinto no tiene solución: -1")
    else:
        print("El camino de longitud mínima tiene longitud " + str(tests[i].evaluar_caminos()[0]))
        tests[i].representar_camino()
