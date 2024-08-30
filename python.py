import numpy as np
from collections import Counter

array = [23, 5, 12, 17, 5, 23, 7, 42, 8, 3, 7, 42, 5, 12, 15, 7]

# n
n = len(array)
#min_value 
min_value = min(array)
#max_value
max_value = max(array)

# nuevo array con los parametros n min_value y max_value
new_array = [n, min_value, max_value]
print(f"Nuevo array con parámetros: {new_array}")

# Calcular y mostrar el promedio
average = np.mean(array)
print(f"Promedio: {average:.2f}")

# Mostrar el valor minimo y máximo
print(f"Valor mínimo: {min_value}")
print(f"Valor máximo: {max_value}")

# Ordenar el array y mostrar el resultado
sorted_array = sorted(array)
print(f"Array ordenado: {sorted_array}")

# Eliminar duplicados y mostrar el array resultante
unique_array = list(set(array))
print(f"Array sin duplicados: {unique_array}")

# Buscar (17) y mostrar la posición
search_value = 17
if search_value in array:
    position = array.index(search_value)
    # Por si el numero si se encuentra en el array
    print(f"El numero {search_value} se encuentra en la posición {position}.")
else:
    # Por si el numero no se encuentra en el array
    print(f"El numero {search_value} no se encuentra en el array.")

# Contar y mostrar las ocurrencias de cada numero
occurrences = Counter(array)
print("Ocurrencias de cada numero:")
for number, count in occurrences.items():
    print(f"Numero {number}: {count} veces")