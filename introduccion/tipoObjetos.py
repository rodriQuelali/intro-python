a = 10           # int
b = 3.14         # float
c = True         # bool
d = "Hello"      # str
e = [1, 2, 3]    # list
f = (1, 2, 3)    # tuple
g = {'a': 1}     # dict
h = {1, 2, 3}    # set
i = None         # NoneType
j = 2 + 3j       # complex

print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j))

#PARA INT
"""
bit_length(): Devuelve el número de bits necesarios para representar el entero en binario.
to_bytes(): Convierte el entero en una secuencia de bytes.
"""
x = 10
print(x.bit_length())  # 4, porque 10 en binario es 1010 (4 bits)

# Convertir el número en 2 bytes
print(x.to_bytes(2, byteorder='big'))  # b'\x00\n'



#PARA FLOAT
"""
as_integer_ratio(): Devuelve una tupla de dos enteros que representan el número como una fracción.
is_integer(): Devuelve True si el valor flotante es un entero.
hex(): Convierte el número flotante a su representación hexadecimal.
"""
y = 3.14
print(y.as_integer_ratio())  # (157, 50), porque 3.14 es 157/50

z = 10.0
print(z.is_integer())  # True

print(y.hex())  # '0x1.91eb851eb851fp+1'

#PARA BOOLEAN
"""
Los booleanos no tienen métodos especiales propios porque son una subclase de int, y se comportan como enteros (True es 1, y False es 0).
"""
a = True
print(a + 1)  # 2, porque True se comporta como 1

#PARA STRING
"""
upper(): Convierte la cadena a mayúsculas.
lower(): Convierte la cadena a minúsculas.
replace(old, new): Reemplaza todas las ocurrencias de una subcadena por otra.
split(): Divide la cadena en una lista de subcadenas.
strip(): Elimina los espacios en blanco al principio y al final de la cadena.
join(iterable): Une los elementos de un iterable con la cadena como separador.
"""
s = "Hello World"
print(s.upper())          # "HELLO WORLD"
print(s.lower())          # "hello world"
print(s.replace("World", "Python"))  # "Hello Python"
print(s.split())          # ['Hello', 'World']
print(s.strip())          # "Hello World" (sin cambios en este caso)
print(", ".join(['a', 'b', 'c']))  # 'a, b, c'

#PARA LIST
"""
append(x): Añade un elemento al final de la lista.
pop([i]): Elimina y devuelve el elemento en la posición i (por defecto, el último).
remove(x): Elimina la primera aparición del valor x.
sort(): Ordena los elementos de la lista.
reverse(): Invierte el orden de los elementos.
extend(iterable): Añade los elementos de un iterable al final de la lista.
"""
lst = [3, 1, 2]
lst.append(4)
print(lst)  # [3, 1, 2, 4]

lst.pop()
print(lst)  # [3, 1, 2]

lst.remove(1)
print(lst)  # [3, 2]

lst.sort()
print(lst)  # [2, 3]

lst.reverse()
print(lst)  # [3, 2]

lst.extend([5, 6])
print(lst)  # [3, 2, 5, 6]

#TUPLAS
"""
Las tuplas son inmutables, por lo que solo tienen algunos métodos.

count(x): Devuelve el número de veces que el valor x aparece en la tupla.
index(x): Devuelve el índice de la primera aparición del valor x.
"""

t = (1, 2, 2, 3)
print(t.count(2))  # 2
print(t.index(3))  # 3

#PARA DICT
"""
keys(): Devuelve una vista de las claves del diccionario.
values(): Devuelve una vista de los valores.
items(): Devuelve una vista de los pares clave-valor.
get(key): Devuelve el valor asociado a la clave, o None si no existe.
update(d): Actualiza el diccionario con los pares clave-valor de otro diccionario o iterable.
pop(key): Elimina la clave y devuelve su valor.
clear(): Vacía el diccionario.
"""
d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())     # dict_keys(['a', 'b', 'c'])
print(d.values())   # dict_values([1, 2, 3])
print(d.items())    # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(d.get('a'))   # 1
d.update({'d': 4})
print(d)            # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d.pop('a')
print(d)            # {'b': 2, 'c': 3, 'd': 4}
d.clear()
print(d)            # {}

#PARA SET
"""
add(x): Añade un elemento al conjunto.
remove(x): Elimina el elemento x (lanza un error si no está presente).
discard(x): Elimina el elemento x si está presente (sin error si no lo está).
union(set): Devuelve un nuevo conjunto con los elementos de ambos conjuntos.
intersection(set): Devuelve un nuevo conjunto con los elementos comunes a ambos conjuntos.
difference(set): Devuelve un conjunto con los elementos que están en el primer conjunto pero no en el segundo.
"""
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

s.remove(4)
print(s)  # {1, 2, 3}

s.discard(3)
print(s)  # {1, 2}

s2 = {2, 3, 4}
print(s.union(s2))          # {1, 2, 3, 4}
print(s.intersection(s2))   # {2}
print(s.difference(s2))     # {1}

#PARA BYTE
"""
decode(): Convierte la secuencia de bytes en una cadena de texto.
hex(): Convierte los bytes en su representación hexadecimal.
"""
b = b'hello'
print(b.decode())  # 'hello'
print(b.hex())     # '68656c6c6f'

#PARA Métodos del tipo NoneType
"""
NoneType no tiene métodos propios, ya que solo tiene un valor posible: None.
"""
x = None
print(type(x))  # <class 'NoneType'>

#PARA COMPLEX
"""
real: Devuelve la parte real del número complejo.
imag: Devuelve la parte imaginaria.
conjugate(): Devuelve el conjugado del número complejo.
"""
z = 1 + 2j
print(z.real)        # 1.0
print(z.imag)        # 2.0
print(z.conjugate()) # (1-2j)

