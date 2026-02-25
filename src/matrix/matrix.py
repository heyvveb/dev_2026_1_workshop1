class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    Incluye operaciones aritméticas, propiedades y transformaciones matriciales.
    """

    def suma_matrices(self, A, B):
        """
        Suma dos matrices elemento a elemento.

        Args:
            A (list): Primera matriz (lista de listas)
            B (list): Segunda matriz (lista de listas), debe tener las mismas dimensiones que A

        Returns:
            list: Matriz resultante de la suma

        Raises:
            ValueError: Si las matrices tienen dimensiones incompatibles

        Ejemplo:
            suma_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) -> [[6, 8], [10, 12]]
        """
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError()

        suma=[]
        for i in range(len(A)):
            fila=[]
            for j in range(len(A[0])):
                fila.append(A[i][j]+B[i][j])
            suma.append(fila)
        return suma
    
        pass

    def resta_matrices(self, A, B):
        """
        Resta dos matrices elemento a elemento (A - B).

        Args:
            A (list): Primera matriz (lista de listas)
            B (list): Segunda matriz (lista de listas), debe tener las mismas dimensiones que A

        Returns:
            list: Matriz resultante de la resta

        Raises:
            ValueError: Si las matrices tienen dimensiones incompatibles

        Ejemplo:
            resta_matrices([[5, 6], [7, 8]], [[1, 2], [3, 4]]) -> [[4, 4], [4, 4]]
        """
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError()

        resta=[]
        for i in range(len(A)):
            fila=[]
            for j in range(len(A[0])):
                fila.append(A[i][j]-B[i][j])
            resta.append(fila)
        return resta        
        pass

    def multiplicar_matrices(self, A, B):
        """
        Multiplica dos matrices usando la multiplicación matricial estándar.
        El número de columnas de A debe ser igual al número de filas de B.

        Args:
            A (list): Primera matriz de dimensiones m x n
            B (list): Segunda matriz de dimensiones n x p

        Returns:
            list: Matriz resultante de dimensiones m x p

        Raises:
            ValueError: Si las dimensiones son incompatibles para multiplicación

        Ejemplo:
            multiplicar_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) -> [[19, 22], [43, 50]]
        """
        if len(A[0]) != len(B):
            raise ValueError()

        multiplicación=[]
        for i in range(len(A)):
            fila=[]
            for j in range(len(B[0])):
                suma=0
                for k in range(len(A[0])):
                    suma+=A[i][k]*B[k][j]
                fila.append(suma)
            multiplicación.append(fila)
        return multiplicación        
        pass

    def multiplicar_escalar(self, matriz, escalar):
        """
        Multiplica cada elemento de la matriz por un escalar.

        Args:
            matriz (list): Matriz (lista de listas)
            escalar (number): Valor escalar por el que se multiplica

        Returns:
            list: Matriz con cada elemento multiplicado por el escalar

        Ejemplo:
            multiplicar_escalar([[1, 2], [3, 4]], 3) -> [[3, 6], [9, 12]]
        """
        
        multiplicacion=[]
        for i in range(len(matriz)):
            fila=[]
            for j in range(len(matriz[0])):
                multi=matriz[i][j]*escalar
                fila.append(multi)
            multiplicacion.append(fila)
        
        return multiplicacion
        pass

    def transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz (intercambia filas por columnas).

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz transpuesta

        Ejemplo:
            transpuesta([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
        """
        if not matriz:
            return []
        transpuesta=[]
        for j in range(len(matriz[0])):
            fila=[]
            for i in range(len(matriz)):
                fila.append(matriz[i][j])
            transpuesta.append(fila)
        
        return transpuesta
        pass

    def es_cuadrada(self, matriz):
        """
        Verifica si una matriz es cuadrada (mismo número de filas y columnas).

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            bool: True si la matriz es cuadrada, False en caso contrario

        Ejemplo:
            es_cuadrada([[1, 2], [3, 4]]) -> True
            es_cuadrada([[1, 2, 3], [4, 5, 6]]) -> False
        """
        if not matriz:
            return False
        if len(matriz)!= len(matriz[0]):
            return False
        return True
        pass

    def es_simetrica(self, matriz):
        """
        Verifica si una matriz es simétrica (igual a su transpuesta).
        Solo aplica a matrices cuadradas.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es simétrica, False en caso contrario

        Ejemplo:
            es_simetrica([[1, 2, 3], [2, 5, 6], [3, 6, 9]]) -> True
            es_simetrica([[1, 2], [3, 4]]) -> False
        """
        for i in range(len(matriz)):
            for j in range(i+1,len(matriz)):
                if matriz[i][j]!=matriz[j][i]:
                    return False
        return True
        pass

    def traza(self, matriz):
        """
        Calcula la traza de una matriz cuadrada (suma de los elementos de la diagonal principal).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            number: La suma de los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            traza([[1, 2], [3, 4]]) -> 5
            traza([[1, 0, 0], [0, 5, 0], [0, 0, 9]]) -> 15
        """
        if len(matriz)!= len(matriz[0]):
            raise ValueError()
        suma=0
        for i in range(len(matriz[0])):
            suma+=matriz[i][i]
        return suma    
        pass

    def determinante_2x2(self, matriz):
        """
        Calcula el determinante de una matriz 2x2.
        det([[a, b], [c, d]]) = a*d - b*c

        Args:
            matriz (list): Matriz 2x2 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 2x2

        Ejemplo:
            determinante_2x2([[3, 8], [4, 6]]) -> -14
            determinante_2x2([[1, 2], [3, 4]]) -> -2
        """
        if len(matriz)!=2 and len(matriz[0])!=2:
            raise ValueError()
        multi=(matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0])
        return multi
        pass

    def determinante_3x3(self, matriz):
        """
        Calcula el determinante de una matriz 3x3 usando la regla de Sarrus.

        Args:
            matriz (list): Matriz 3x3 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 3x3

        Ejemplo:
            determinante_3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 0
            determinante_3x3([[1, 0, 0], [0, 2, 0], [0, 0, 3]]) -> 6
        """
        if len(matriz)!=3 or len(matriz[0])!=3:
            raise ValueError()
        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[0][2]
        d = matriz[1][0]
        e = matriz[1][1]
        f = matriz[1][2]
        g = matriz[2][0]
        h = matriz[2][1]
        i = matriz[2][2]

        determinante = (
            (a*e*i) + (b*f*g) + (c*d*h)
          - (c*e*g) - (b*d*i) - (a*f*h)
        )
        return determinante
        pass

    def identidad(self, n):
        """
        Genera una matriz identidad de tamaño n x n.
        La diagonal principal tiene 1s y el resto 0s.

        Args:
            n (int): Tamaño de la matriz identidad

        Returns:
            list: Matriz identidad n x n

        Ejemplo:
            identidad(2) -> [[1, 0], [0, 1]]
            identidad(3) -> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        """
        matriz=[]
        for i in range(0,n):
            fila=[]
            for j in range(0,n):
                if i ==j:
                    fila.append(1)
                else:
                    fila.append(0)
            matriz.append(fila)
        return matriz
        pass

    def diagonal(self, matriz):
        """
        Extrae los elementos de la diagonal principal de una matriz cuadrada.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            list: Lista con los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 5, 9]
            diagonal([[3, 0], [0, 7]]) -> [3, 7]
        """
        if len(matriz)!= len(matriz[0]):
            raise ValueError
        
        diagola=[]
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if i==j:
                    diagola.append(matriz[i][j])
        return diagola
        pass

    def es_diagonal(self, matriz):
        """
        Verifica si una matriz cuadrada es diagonal
        (todos los elementos fuera de la diagonal principal son cero).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es diagonal, False en caso contrario

        Ejemplo:
            es_diagonal([[3, 0], [0, 7]]) -> True
            es_diagonal([[1, 2], [0, 4]]) -> False
        """
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if i!=j:
                    if matriz[i][j]!=0:
                        return False
        return True
        pass

    def rotar_90(self, matriz):
        """
        Rota una matriz 90 grados en sentido horario.

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz rotada 90 grados en sentido horario

        Ejemplo:
            rotar_90([[1, 2], [3, 4]]) -> [[3, 1], [4, 2]]
            rotar_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        rotada=[]
        for j in range(len(matriz[0])):
            fila=[]
            for i in range(len(matriz)-1,-1,-1):
                fila.append(matriz[i][j])
            rotada.append(fila)

        return rotada
        pass

    def buscar_en_matriz(self, matriz, valor):
        """
        Busca un valor en la matriz y retorna todas las posiciones donde se encuentra.

        Args:
            matriz (list): Matriz (lista de listas)
            valor: Valor a buscar en la matriz

        Returns:
            list: Lista de tuplas (fila, columna) con las posiciones del valor.
                  Retorna lista vacía si no se encuentra.

        Ejemplo:
            buscar_en_matriz([[1, 2, 3], [4, 2, 6], [7, 8, 2]], 2) -> [(0, 1), (1, 1), (2, 2)]
            buscar_en_matriz([[1, 2], [3, 4]], 9) -> []
        """
        posición=[]
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                    if matriz[i][j]==valor:
                        posición.appen((i,j))
        return posición
        pass
