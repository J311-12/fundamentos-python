# 1.Defininiendo una variable por cada tipo de dato primitivo

# Definición de variables de diferentes tipos primitivos
entero = 10
flotante = 3.14
booleano = True
string = 'A'

# Concatenación de variables a una cadena
cadena_resultante = "El valor de 'entero' es: " + str(entero) + "\n"
cadena_resultante += "El valor de 'flotante' es: " + str(flotante) + "\n"
cadena_resultante += "El valor de 'booleano' es: " + str(booleano) + "\n"
cadena_resultante += "El valor de 'String' es: " + string

# Imprimir el resultado
print(cadena_resultante)


# 2.Limite de los Enteros y flotantes :

# El límite de los enteros y los flotantes se refiere a los valores máximos y mínimos que pueden representar cada uno de estos tipos de datos en un lenguaje de programación.

# En el caso de los enteros, su límite está determinado por la capacidad de almacenamiento del tipo de dato utilizado. Dependiendo de la arquitectura y del lenguaje de programación, el rango de valores enteros puede variar. En general, los enteros suelen poder representar números desde -2^(n-1) hasta 2^(n-1)-1, donde n es el número de bits utilizados para almacenar el entero. Por ejemplo, en el caso de los enteros de 32 bits, el rango típico sería desde -2,147,483,648 hasta 2,147,483,647.

# Por otro lado, los flotantes representan números con parte decimal y su límite está determinado por la precisión finita del tipo de dato utilizado. Los flotantes se almacenan en forma de aproximaciones y, debido a la naturaleza de la representación en punto flotante, pueden presentar errores de redondeo. Los flotantes de doble precisión (64 bits) suelen ser comunes y pueden representar números con una magnitud de alrededor de 1.8 × 10^308 y una precisión de aproximadamente 15 dígitos decimales significativos.

# Es importante tener en cuenta estos límites al trabajar con enteros y flotantes, ya que superarlos puede conducir a resultados inexactos o incluso errores en los cálculos.



# 3.Aplicando la formula de suma de los primeros n numeros

n = int(input("Ingresa el valor de n: "))  # Solicitamos al usuario el valor de n como un número entero

suma = n * (n + 1)  # Aplicamos la fórmula directa para calcular la suma de los primeros n números pares
resultado = suma - (n % 2) * n  # Ajustamos el resultado utilizando el residuo de n dividido por 2

print("La suma de los primeros", n, "números pares es:", resultado)  # Imprimimos el resultado
