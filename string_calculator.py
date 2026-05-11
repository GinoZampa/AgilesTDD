def sumar(numbers: str) -> int:
    if numbers == "":
        return 0
    elif "," in numbers:
        numeros = numbers.split(",")
        return int(numeros[0]) + int(numeros[1])
    else:
        return int(numbers)
    
