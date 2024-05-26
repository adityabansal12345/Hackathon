import random as rd 

flashcard = {}
flash_amount = int(input('How many flashcards do you require: '))
if flash_amount <= 3:
    print("You need at least 4 flashcards")
else:
    pass



for i in range(flash_amount):
    key = input(f'Enter flashcard {i} reference name: ')
    value = input('Enter flashcard definition: ')
    flashcard[key] = value
a=0
def test():
    global a
    global flash_amount
    print(flashcard)
    for key, value in rd.choice(flashcard.items()):  
        ans = input(f'what does {key} mean: ') 
        real_ans = value
        print(real_ans)
        if ans==real_ans:
            print('Correct')
            a+=1
        else:
            print("Incorrect")
            a+=0
        print(f'You got {a} out of {flash_amount} correct')  