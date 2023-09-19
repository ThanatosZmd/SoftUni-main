book_search = input()
curr_book = input()
counter = 0
while True:
    if curr_book=='No More Books':
        print('The book you search is not here!\n'
                f'You checked {counter} books.')
        break
    elif curr_book!=book_search:
        counter+=1
        curr_book = input()
    else:
        print(f'You checked {counter} books and found it.')
        break