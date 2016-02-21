#Automate the Boring Stuff Chapter 3
#Collatz Conjecture
def collatz():
    
    print('Enter a number, and it will become 1 in no time! ')
    number = int(input())
    
    while number > 1:
        if number % 2 == 0:
            number = number //2
            print(str(number))
            
        else:
            number = 3*number + 1 
            print(str(number))

collatz()