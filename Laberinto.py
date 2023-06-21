class Laberinto:
    def __init__(self, filas, columnas, walls=[]):
        """ Construye  el laberinto con n filas, m columnas i las paredes en las posiciones indicadas en walls,
        que es una lista de tuplas (fila, columna)."""
        self.__f = filas
        self.__c = columnas
        self.__walls = walls
        self.__l = []

        for i in range(self.__f):
            f = []
            for j in range(self.__c):
                f.append('.')
            self.__l.append(f)

        if len(self.__walls) >0:
            for w in self.__walls:
                self.__l[w[0] - 1][w[1] - 1] = '#'

        """Ponemos la posición inicial del rectángulo, que según el problema siempre es la misma, pero 
        consideramos el caso en que no se pueda empezar en horizontal y se tenga que empezar en verical."""
        if self.__l[0][1] == '#':
            self.__pos_r = [1, 0]
            self.__orientation = 'v'
        else:
            self.__pos_r = [0, 1]
            self.__orientation = 'h'

    def puedo_bajar(self, o, pos):
        """ Determina si puede bajar a la casilla inferior de su posició (pos) en función de su orientación.
        pos és una tupla con las cordenadas de su posición: (fila, columna)."""

        if o == 'h':
            if pos[0] == self.__f-1:
                return 0
            for i in range(3):
                if self.__l[pos[0]+1][pos[1]-1+i] == '#':
                    return 0
            return 1
        else:
            if pos[0] == self.__f-2:
                return 0
            elif self.__l[pos[0]+2][pos[1]] == '#':
                return 0
            return 1

    def puedo_derecha(self, o, pos):
        """ Determina si puede ir a la derecha de su posició (pos) en función de su orientación.
                pos és una tupla con las cordenadas de su posición: (fila, columna)."""

        if o == 'h':
            if pos[1] == self.__c-2:
                return False
            elif self.__l[pos[0]][pos[1]+2] == '#':
                return False
            return True
        else:
            if pos[1] == self.__c-1:
                return False
            for i in range(3):
                if self.__l[pos[0]-1+i][pos[1]+1] == '#':
                    return False
            return True

    def puedo_girar(self, pos):
        """ Determina si puede girar respecto su posición, es decir,
        compuerba estar en el centro de una parrilla 3x3."""
        if pos[0] == 0 or pos[0] == self.__f-1 or pos[1] == 0 or pos[1] == self.__c-1:
            return False
        for i in range(3):
            for j in range(3):
                if self.__l[pos[0]-1+i][pos[1]-1+j] == '#':
                    return False
        return True

    def final(self):
        """ Devuleve la posición final objetivo segun el laberinto."""
        if self.__l[self.__f - 2][self.__c - 1] == '#':
            return [self.__f-1, self.__c-2, 'h'], False
        elif self.__l[self.__f - 1][self.__c-2] == '#':
            return [self.__f-2, self.__c-1, 'v'], False
        else:
            return [self.__f-2, self.__c-1, 'v'], [self.__f-1, self.__c-2, 'h']

    def encontrar_caminos(self):
        pos_ini = [self.__pos_r[0], self.__pos_r[1], self.__orientation]
        pos_final1, pos_final2 = self.final()
        camino = []
        lista_caminos = []
        cola = [(pos_ini, camino)]
        visitados = []

        while len(cola)>0:
            camino_act = cola[0][1]
            pos_act = cola.pop(0)[0]
            if pos_act == pos_final1 or pos_act == pos_final2:
                lista_caminos.append(camino_act + [pos_act])
            else:
                if self.puedo_bajar(pos_act[2], pos_act):
                    casilla = [pos_act[0]+1, pos_act[1], pos_act[2]]
                    if casilla not in visitados:
                        visitados.append(casilla)
                        cola.append((casilla, camino_act+[pos_act]))
                if self.puedo_derecha(pos_act[2], pos_act):
                    casilla = [pos_act[0], pos_act[1]+1, pos_act[2]]
                    if casilla not in visitados:
                        visitados.append(casilla)
                        cola.append((casilla, camino_act+[pos_act]))
                if self.puedo_girar(pos_act):
                    if pos_act[2] == 'h':
                        casilla = [pos_act[0], pos_act[1], 'v']
                        if casilla not in visitados:
                            visitados.append(casilla)
                            cola.append((casilla, camino_act + [pos_act]))
                    else:
                        casilla = [pos_act[0], pos_act[1], 'h']
                        if casilla not in visitados:
                            visitados.append(casilla)
                            cola.append((casilla, camino_act+[pos_act]))
        return lista_caminos

    def evaluar_caminos(self):
        """ De la lista de caminos, determina cual es el mas corto o si no tiene solución devuelve -1"""
        caminos = self.encontrar_caminos()
        if len(caminos) == 0:
            return -1
        min_len = len(caminos[0])-1
        idx = 0
        for i in range(1, len(caminos)):
            if len(caminos[i])-1 < min_len:
                min_len = len(caminos[i])-1
                idx = i
        return min_len, idx

    def representar_camino(self):
        camino = self.encontrar_caminos()[self.evaluar_caminos()[1]]
        for paso in camino:
            self.__l[paso[0]][paso[1]] = '*'
            if paso[2] == 'h':
                self.__l[paso[0]][paso[1]-1] = '*'
                self.__l[paso[0]][paso[1]+1] = '*'
            else:
                self.__l[paso[0]-1][paso[1]] = '*'
                self.__l[paso[0]+1][paso[1]] = '*'
            print(self)
            self.clean()

    def clean(self):
        """ Restaura las casillas del laberinto"""
        for i in range(self.__f):
            for j in range(self.__c):
                if self.__l[i][j] == '*':
                    self.__l[i][j] = '.'

    def __str__(self):
        s = ''
        for i in range(self.__f):
            for j in range(self.__c):
                s += self.__l[i][j] + ' '
            s += '\n'
        return s


