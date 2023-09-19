product = input()
fruits = ['banana','apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegies= ['tomato','cucumber','pepper','carrot']
if product in fruits:
    print('fruit')
elif product in vegies:
    print('vegetable')
else:
    print('unknown')