# TODO Найдите количество книг, которое можно разместить на дискете

total_capacity = 1.44 * 1024 * 1024 # in bytes
book_capacity = 100 * 50 * 25 * 4 # in bytes

print("Количество книг, помещающихся на дискету:", int(total_capacity//book_capacity))
