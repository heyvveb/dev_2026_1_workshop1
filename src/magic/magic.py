class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        numeros=[0,1]
        fibona=0
        if n<0:
            return None
        if n==0:
            return 0
        if n<3:
            return 1
        for i in range(n-1):
            fibona=numeros[i]+numeros[i+1]
            numeros.append(fibona)
        return fibona
        pass
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        numeros=[0,1]
        fibona=0
        if n==0:
            return []
        if n==1:
            return [0]
        for i in range(n-2):
            fibona=numeros[i]+numeros[i+1]
            numeros.append(fibona)
        return numeros
        pass
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        p=0
        if n<2:
            return False
        for i in range(1,n+1):
            if n%i==0:
                p+=1
        if p==2:
            return True
        return False
        pass
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        primos=[]
        p=0
        for j in range(2,n+1):
            p=0
            for i in range(1,j+1):
                if j%i==0:
                    p+=1
                if p==2:
                    primos.append(j)
        return primos

        pass
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        for i in range(n-1):
            if n%i==0:
                suma+=i
        return suma==n
        pass
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        triangulo =[]
        for i in range(filas):
            fila = [1]*(i+1)
            for j in range(1,i):
                fila[j]=triangulo[i-1][j-1]+triangulo[i-1][j]
            triangulo.append(fila)

        return triangulo
        pass
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        fac=0
        if n==0:
            return 1
        for i in range(n-1):
            fac=i*(i+1)
        return fac
        pass
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b!=0:
            residuo=a%b
            a=b
            b=residuo
        return a
        pass
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        x=a
        y=b
        while b!=0:
            residuo=a%b
            a=b
            b=residuo
        mcd=a
        return (x*y)//mcd
        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        suma=0
        while n>0:
            suma +=n%10
            n//=10
        return suma
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        suma=0
        numero=n
        while n>0:
            suma += (n%10)**3
            n//=10
        return suma==numero
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n=len(matriz)
        numero=sum(matriz[0])

        for fila in matriz:
            if sum(fila) != numero:
                return False
        for col in range(n):
            for fila in range(n):
                if sum(matriz[fila][col]) != numero:
                    return False
        for i in range(n):
            if sum(matriz[i][i])!=numero:
                return False
        for i in range(n):
            sum(matriz[i][n-1-i])!=numero
            return False
        return True
        pass