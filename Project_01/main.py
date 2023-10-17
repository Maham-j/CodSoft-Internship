# calculatorn     
logo = '''            _            _       _                 
   ___ __ _| | ___ _   _| | __ _| |_ ___  _ ___  
  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__/
 | (_| (_| | | (__| |_| | | (_| | || (_) | |  
  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  
 
 _____________________
|  _________________  |
| | MJ           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''

from IPython.display import clear_output
def add(n1,n2):
    return n1+n2
    
def subtract(n1,n2):
    return n1-n2
    
def multiply(n1,n2):
    return n1*n2
    
def divide(n1,n2):
    return n1/n2
    
operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}

def calculator():
    print(logo) 
    num1 = float(input('Enter the first number: '))
    for symbol in operations:
        print(symbol)
        
    while True:
        operation_symbol = input('Pick an operation from line above: ')
        num2 = float(input('\n'+'What"s the next number: '))
        oper = operations[operation_symbol]
        answer = oper(num1,num2)
        
        print(f'{num1} {operation_symbol} {num2} = {answer}'+'\n')
        
        clear_output(wait=True)
        again = input(f'Type "y" to continue calculating with {answer} or type "e" to exit or "n" to start-over : ') 
        if again == 'y':
            print(logo)
            num1 = answer
        if again == 'e':
            clear_output(wait=True)
            print(logo)   
            print('Goodbye')
            print(f'The Answer is: {answer}')
            break
        elif again == 'n':
            clear_output(wait=True)
            print(logo)
            num1 = float(input('Enter the first number: '))
calculator()
