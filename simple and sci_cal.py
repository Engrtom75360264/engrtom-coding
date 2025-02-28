import math

def simple_calculator():
    print('\nSimple Calculator')
    print('Operations: +,-,*,/')
    try:
        num1 = float(input('enter first num'))
        operator = input('enter operator(+,-,*,/):')
        num2 = float(input('enter the second num'))
        if operator == '+':
            print('result:',num1 + num2)
        elif operator == '-':
            print('result:',num1-num2)
        elif operator == '*':
            print('result:',num1 *num2)
        elif operator == '/':
            if num2 == 0:
                print('error division by zero')
            else:
                prit('result',num1/num2)
        else:
            print('invalid operator')

    except ValueError:
        print('invalid input! pls enter num only')

def scientific_calculator():
    print('\nscientific calculator')
    print('1. square root(x)')
    print('2. exponential(x)')
    print('3. logarithm(x)')
    print('4. sine(x)')
    print('5. cosine(x)')
    print('6. tangent(x)')

    try:
        choice = int(input('choose an operation(1-6):'))
        num = float(input('enter a num'))
        if choice ==1:
            print('sqrt:'.format(num,math.sqrt(num)))
        elif choice == 2:
            print('exponent:'.format(num,math.exp(num)))
        elif choice == 3:
            if num <=0:
                print('error: logarithm undefined for non-positive numbers')
            else:
                print('log({})={}'.format(num,math.log(num)))
            print('log:'.format(num,math.log(num)))
        elif choice == 4:
            print('sin({})={}:'.format(num,math.sin(math.radians(num))))
        elif choice == 4:
            print('cos({})={}:'.format(num,math.cos(math.radians(num))))
        elif choice == 4:
            print('tan({})={}:'.format(num,math.tan(math.radians(num))))
        else:
            print('invalid choice')

    except ValueError:
        print('invalid input pls enter num only')

def main():
    while True:
        print('\ncalculator menu')
        print('1. simple calculator')
        print('2. scientific calculator')
        print('3. exit')

        try:
            choice = int(input('choose an option:'))
            if choice ==1:
                simple_calculator()
            elif choice ==2:
                scientific_calculator()
            elif choice == 3:
                print('exit calculator, goodbye')
                break
            else:
                print('invalid choice! pls enter 1,2 or 3')
        except ValueError:
            print('invalid input! pls enter a num')


if __name__ == '__main__':
    main()

    
        
        


