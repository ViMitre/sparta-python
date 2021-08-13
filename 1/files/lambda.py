# Lambda

add = lambda n1, n2: n1 + n2
print(add(2, 4))


# Map

def double_add_one(n):
    return (n * 2) + 1


nums = [1, 2, 3, 4, 5]

new_nums = map(double_add_one, nums)
print(list(new_nums))

newer_nums = list(map(lambda n: n*2+1, nums))
print(newer_nums)

savings = [234.00, 555.00, 674.00, 78.00]
# Add 10% with map and lambda

plusten = list(map(lambda n: n+n/10, savings))

print(plusten)

# Filter

def is_even(n):
    return n % 2 == 0

# Filter keeps elements that are TRUE
print(list(filter(is_even, nums)))

# With lambda
even = list(filter(lambda n: n % 2 == 0, nums))
print(even)

print(list(filter(lambda n: n % 2 == 0, range(200))))

# List comprehension

savings = [234.00, 555.00, 674.00, 78.00]
bonus = [x + x /10 for x in savings]
print(bonus)

large_savings = [x for x in savings if x > 500]
print(large_savings)

large_savings_bonus = [x + x /10 for x in savings if x > 500]
print(large_savings_bonus)