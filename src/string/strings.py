class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_nuevo=''
        if not texto:
            return True
        for c in texto:
            if c.isalnum():
                texto_nuevo += c.lower()

        return texto_nuevo == texto_nuevo[::-1]
        pass
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        texto_nuevo=''
        if not texto:
            return ""
        for c in texto[::-1]:
            texto_nuevo+=c
        return texto_nuevo
        pass
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
            
        Args:
            texto (str): Cadena para contar vocales
                
        Returns:
            int: Número de vocales en la cadena
        """
        vocal=['a','e','i','o','u']
        contador=0
        for letra in texto.lower():
            if letra in vocal:
                contador+=1
        return contador
        pass
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        conosonante=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        contador=0
        for letra in texto.lower():
            if letra in conosonante:
                contador+=1
        return contador
        pass
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        texto1=texto1.replace(" ","").lower()
        texto2=texto2.replace(" ","").lower()
        return sorted(texto1)==sorted(texto2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        palabras=texto.split()
        return len(palabras)
        pass
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
            
        Args:
            texto (str): Cadena
                
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        resultado = []
        nueva_palabra = True 

        for c in texto:
            if c == " ":
                resultado.append(c)
                nueva_palabra = True
            else:
                if nueva_palabra:
                    resultado.append(c.upper())
                    nueva_palabra = False
                else:
                    resultado.append(c)
        
        return "".join(resultado)
        pass
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        inicio = 0
        while inicio < len(texto) and texto[inicio] == " ":
            inicio += 1
        espacios_inicio = texto[:inicio]

        fin = len(texto) - 1
        while fin >= 0 and texto[fin] == " ":
            fin -= 1
        espacios_fin = texto[fin+1:]

        medio = texto[inicio:fin+1] if fin >= inicio else ""

        resultado_medio = []
        anterior_espacio = False
        for c in medio:
            if c == " ":
                if not anterior_espacio:
                    resultado_medio.append(c)
                anterior_espacio = True
            else:
                resultado_medio.append(c)
                anterior_espacio = False
        
        return espacios_inicio + "".join(resultado_medio) + espacios_fin

        pass
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if texto[0] in ('-', '+'):
            if len(texto) == 1:
                return False
            texto = texto[1:]
        for caracter in texto:
            if caracter < '0' or caracter > '9':
                return False
        return True
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado=""
        for caracter in texto:
            if 'a' <= caracter <= 'z':
                nueva_letra =chr((ord(caracter)-ord('a')+desplazamiento)%26 +ord('a'))
                resultado += nueva_letra
            elif 'A' <= caracter <= 'Z':
                nueva_letra = chr((ord(caracter) - ord('A') + desplazamiento) % 26 + ord('A'))
                resultado += nueva_letra
            else:
                resultado += caracter
        return resultado
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        resultado = ""

        for char in texto:
            if char.isupper(): 
                resultado += chr((ord(char) - 65 - desplazamiento) % 26 + 65)
            elif char.islower():  
                resultado += chr((ord(char) - 97 - desplazamiento) % 26 + 97)
            else:
                resultado += char
        
        return resultado
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if not subcadena:
            return []
    
        posiciones = []
        n = len(texto)
        m = len(subcadena)
        
        for i in range(n - m + 1):

            coincidencia = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    coincidencia = False
                    break
            if coincidencia:
                posiciones.append(i)
        
        return posiciones
        pass