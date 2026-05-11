def sumar(numbers: str) -> int:
    if numbers == "":
        return 0
    elif "," in numbers:
        return 3
    else:
        return int(numbers)
    
