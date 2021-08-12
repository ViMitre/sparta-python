def add(*multiargs: int) -> int:
    return sum(multiargs)

def subt(int1: int, int2: int) -> int:
    return int1-int2

def mult(int1: int, int2: int) -> int:
    return int1*int2

def div(int1: int, int2: int) -> int:
    return int1/int2

# print(add(24, 32, 64))
# print(subt(43, 11))
# print(mult(5, 8))
# print(div(60, 6))

def calc(instruction, int1: int, int2: int) -> int:
    if instruction == "add":
        return add(int1, int2)
    if instruction == "subtract":
        return subt(int1, int2)
    if instruction == "multiply":
        return mult(int1, int2)
    if instruction == "divide":
        return div(int1, int2)


# calc("add", 5, 8)