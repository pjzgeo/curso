# escribir un programa que lea un número entero positivo y muestre en pantalla la suma de los dígitos de dicho número.
# Ejemplo: si el número es 123, la suma sería 1 + 2 + 3 = 6


# Función que suma los dígitos de un número
def suma_digitos(n):
    suma = 0
    while n != 0:
        suma += n % 10
        n = n // 10
    return suma

# Función principal
def main():
    n = int(input("Ingrese un número entero positivo: "))
    while n < 0:
        n = int(input("Ingrese un número entero positivo: "))
    print(f"La suma de los dígitos de {n} es {suma_digitos(n)}")

if __name__ == "__main__":
    main()



