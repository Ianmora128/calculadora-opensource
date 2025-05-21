from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    while True:
        print("\n--- Calculadora OpenSource ---")
        print("1. Sumar 2 números")
        print("2. Restar 2 números")
        print("3. Multiplicar 2 números")
        print("4. Dividir 2 números")
        print("5. Suma avanzada (varios números)")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", sumar(a, b))

        elif opcion == "2":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", restar(a, b))

        elif opcion == "3":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", multiplicar(a, b))

        elif opcion == "4":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            if b != 0:
                print("Resultado:", dividir(a, b))
            else:
                print("Error: No se puede dividir entre cero.")

        elif opcion == "5":
            numeros = input("Introduce los números separados por espacio: ")
            lista = list(map(float, numeros.split()))
            print("Resultado:", suma_avanzada(lista))

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()