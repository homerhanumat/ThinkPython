a = int(input('Enter a value for a\n'))
b = int(input('\nEnter a value for b\n'))
c = int(input('\nEnter a value for c\n'))
n = int(input('\nEnter a value for n\n'))

print('\nProposed Equation:\t',
      a,'^',n,' + ',b,'^',n, ' = ',c,'^',n,'\n',sep='')

if n > 2 and a**n+b**n==c**n:
    print("Fermat was wrong!")
elif n<=2 and a**n+b**n==c**n:
    print("The equation is true, but does not contradict",
          " Fermat's conjecture.",sep='')
else:
    print("The equation isn't true.")
