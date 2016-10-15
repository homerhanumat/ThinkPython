import math

def eval_loop():
    prev_expr = 0
    while True:
        expr = input('Enter a string to evaluate:  ')
        if expr == 'done':
            return eval(prev_expr)
        print(eval(expr))
        prev_expr = expr

#a=eval_loop()
#print(a)

# Let's try some error-handling:

def eval_loop2():
    prev_expr = 0
    while True:
        expr = input('Enter a string to evaluate:  ')
        if expr == 'done':
            return eval(prev_expr)
        try:
            print(eval(expr))
        except:
            print('For some reason tha expression was not',
                  'valid:  try again.')
            continue
        prev_expr = expr

eval_loop2()
