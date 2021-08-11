def square_add_one(num):
    result = num ** 2
    def add_one(result):
        result += 1
        return  result
    result = add_one(result)
    return result


print(square_add_one(4))

# print(result)