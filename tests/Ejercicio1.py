#Escribir un programa que dado el ingreso de un numero retorne si el mismo es primo o no.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    numero = int(input("Ingrese un numero: "))
    if es_primo(numero):
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")