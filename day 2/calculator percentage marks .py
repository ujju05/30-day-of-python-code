# calculating compound interest


p=float(input('enter the principal value ='))
r=float(input('enter the interset rate ='))
t=float(input('enter the period ='))


ci=p*(pow((1+r/100),t))

print("compound interest =",ci)

# programe for calculating percentage

v=float(input('enter the obatain value ='))
x=float(input('enter the total value ='))

p=((v/x)*100)
print('percentage =',p,'%')

# programe for printing last,and first value

a=str(input('enter the word ='))
print(a[0:1])
print(a[-1])






