# Test #

Las siguientes preguntas corresponden a un set de skills básicas que se solicita poseer a los desarrolladores de OSA SPA 

### 1 Desarrollo ###

Implementar un reloj que sea capaz de manejar horas sin fechas. Debe ser capaz de agregarle y restarle minutos.
Como input recibirá dos integer (hora, minutos). Retornará un string con la hora que representa. Se toma como base las '00:00'.

Al desarrollar, crear casos de prueba.

Ejemplo de Pruebas

input-> Output:

==========================

 * Reloj(8,0) -> '08:00'
 * Reloj(72,8640) -> '00:00'
 * Reloj(-1,15) -> '23:15'
 * Reloj(-25,-160) -> '20:20'
 * Reloj(10,3).suma(-70) -> '08:53'

==========================



### 2 Desarrollo de API ###
Si alguna vez has utilizado la API de Facebook, sabrás lo común que "deprecaban" su API. Según usted:

* Explique la razón por la cuál esta no es una buena práctica.
* ¿Por qué se dice que las interfaces deben ser "tontas"?
* Como aplicaria usted los conceptos de Encapsulamiento, Flexibilidad, Seguridad y Versionamiento en el desarrollo de una Interfaz?




### 3 Comprensión ###

Con el siguiente código en python:


    # -*- coding: utf-8 -*-
    def z(c):
        if c[-1] == '?':
    	    return 3
    	else:
    	    return 2
    
    def y(b):
        r = [l.isupper() for l in b[:-1] if l.isalpha()]
    
        if r and reduce(lambda a,x : a and x, r): # !
            return 4
        else:
            return z(b)
    
    
    def x(a):
        a = ''.join(a.strip().split(' '))
        return y(a) if a else 1


Llamadas:

* x('')
* x('1 2 3 4')
* x('1 2 3 4 A?')
* x('hola?')
* x('HOLA')


Explique según usted:

* ¿Qué hace este código?
* ¿En la lí­nea marcada con un # !: ¿Qué problema se puede presentar? ¿cómo se soluciona?
* ¿Qué mejora harí­a usted en la implementación del código?

### 4 Django ###

Explique con sus palabras qué diferencias tiene hacer un _prefetch_related_ y un _select_related_.

* ¿Cuándo usarías cada uno?
* Dé un ejemplo de cuándo sería conveniente usar una u otra.


### Entrega ###

Cualquier suposición, dejarla cláramente estipulada.

Recuerda, es sólo una prueba que quiere ver tu proceso de pensamiento y NADA dice de como eres como persona, por lo tanto no le dediques más de 90 minutos.  

Disfruta!!!


-----------------------------------