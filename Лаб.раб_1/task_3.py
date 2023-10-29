# TODO Найдите количество книг, которое можно разместить на дискете

disk_vol = 1.44     # объем дискеты в Мб
disk_vol_bytes = (disk_vol * 1024) * 1024

pages_num = 100    # число страниц в книге

verses_num = 50    # число строк на странице

symbols_num = 25    # число символов на странице

one_symbol_vol = 4    # память на один символ (байт)

one_book_vol = one_symbol_vol * symbols_num * verses_num * pages_num

books_num = int(disk_vol_bytes // one_book_vol)

print("Количество книг, помещающихся на дискету:", books_num)
