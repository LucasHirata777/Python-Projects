def fizzBuzz(n):
    # Write your code here
    for n in range(1,n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)
while True:
    n = int(input('Type a number: ').strip().upper())
    if n == 0:
        break


    fizzBuzz(n)
print('O programa finalizou!')
