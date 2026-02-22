class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        n=[]
        i= len(lista)-1
        while i >= 0:
            n.append(lista[i])
            i-=1
        return n
        pass
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        i=0
        for n in lista:
            if n==elemento:
                return i
            i+=1
            
        return -1
        pass
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        n=[]
        for i in range(len(lista)):
            c=0
            for j in range(len(n)):
                if lista[i]==n[j] and type(lista[i]) == type(n[j]):
                    c+=1
            if c==0:
                n.append(lista[i])
        return n
        pass
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        n=[]
        i=0
        j=0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                n.append(lista1[i])
                i += 1
            else:
                n.append(lista2[j])
                j += 1
        while i < len(lista1):
            n.append(lista1[i])
            i += 1

        while j < len(lista2):
            n.append(lista2[j])
            j += 1
        return n
        pass
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        n=[]
        for i in range(len(lista)):
            p=i-k%len(lista)
            n.append(lista[p])
        return n
        pass
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        for i in range(len(lista)-1):
            if (lista[i+1]-lista[i])!=1:
                return 1+lista[i]
        if lista[0] !=1:
            return 1
        return lista[-1] + 1
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        c=0
        for i in range(len(conjunto2)):
            for j in range(len(conjunto1)):
                if conjunto1[j]==[conjunto2[i]]:
                    c+=1
        if c==len(conjunto1):
            return True
        else:
            return False
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila=[]

        def push(elemento):
            pila.append(elemento)
        def pop():
            if len(pila)==0:
                return None
            return pila.pop()
        def peek():
            return pila[-1]
        def is_empty():
            return len(pila) == 0
        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola=[]

        def enqueue(elemento):
            cola.append(elemento)
        def dequeue():
            if len(cola)==0:
                return None
            return cola.dequeue()
        def peek():
            return cola[0]
        def is_empty():
            return len(cola) == 0
        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }        
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        filas= len (matriz)
        columnas= len(matriz[0])
        t=[]
        for j in range(columnas):
            f=[]
            for i in range(filas):
                f.append(matriz[i][j])
            t.append(f)
        return t
        pass