data = int(input("enter a number "))

def fizzbuzz(n):
    for i in range(n):
        if i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 and i % 5 == 0:
            print('fizzbuzz')
        else: print(i)    

fizzbuzz(data)