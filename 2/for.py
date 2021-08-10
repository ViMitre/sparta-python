# nested_list = [[1, 2, 3], [4, 5], [6]]
#
# for x in nested_list:
#     print(x)
#     for y in x:
#         print(y)

# book = {
#     "name": "The Iliad",
#     "author": "Homer",
#     "rating": 7
# }
#
# for key, value in book.items():
#     print(f"The {key} is {value}")

library = [
    {
    "title": "The Iliad",
    "author": "Homer",
    "rating": 7
    },
    {
    "title": "The foundation of mathematics",
    "author": "Ian Stewart & David Tall",
    "rating": 8.5
    },
    {
    "title": "The Hungry Caterpillar",
    "author": "Eric Carle",
    "rating": 10,
    "synopsis": "The caterpillar eats a lot and transforms."
    }
]

for book in library:
    if "synopsis" in book.keys():
        print(f"{book['title']}: {book['synopsis']}")


