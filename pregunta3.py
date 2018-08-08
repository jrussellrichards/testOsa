from functools import reduce

def z(c):
    if c[-1] == '?': #Si el último caracter es "?" entonces retorna 3, en otro caso retorna 2
        return 3
    else:
        return 2

def y(b):
    r = [l.isupper() for l in b[:-1] if l.isalpha()] #Para cada caracter alfabético en el string (menos el último caracter)
    #se verifican si los valores son mayúsculas y se devuelven los valores de verdad asociados
    if r and reduce(lambda a,x : a and x, r): # Si todos los valores en r son verdaderos, es decir el String b contenía solo mayúsculas
        #en sus valores alfabéticos entonces retorna 4, en otro caso retorna z con el string correspondiente
        return 4
    else:
        return z(b)


def x(a):
    a = ''.join(a.strip().split(' '))  #Se eliminan los espacios. la modificación que haría sería eliminar el strip.   
    return y(a) if a else 1 #En caso de recibir un string vacío se retorna 1, en otro caso se llama a la función y con el string modificado (sin espacios)

if __name__ == "__main__":
    print(x(''),x('1 2 3 4'),x('1 2 3 4 A?'),x('hola?'),x('?'))
    # a='1 2 3 4'
    # a=a.strip()
    # print("a",a)
    # print(x('1 2 3 4 '))

#El programa hace lo siguiente: 
#Retorna 1 en caso de recibir un string vacío 
#retorna 2 en caso de que la cadena recibida no contenga todas las letras Mayúsculas y el último valor no sea "?"
#Retorna 3 en caso de que a cadena no contenga todas las letras mayúsculas pero que el último caracter en la lista sea "?"
#Retorna 4 si todas las letras en el String son mayúsculas

#Problemas
#Si el último valor del String es un loweCase, el algoritmo retorna 4. Esto se debería corregir recorriendo completamente el string en la línea 10. 
#La función strip no está haciendo nada actualmente. 
#En la línea indicada el error encontrado es el siguiente: Se calcula el producto de todos los literales lo que en cadenas grandes requiere mayor tiempo
#de cómputo que recorrer el arreglo y detenerse cuando encuentre un valor lowerCase: Complejidad O(n) vs O(k).

