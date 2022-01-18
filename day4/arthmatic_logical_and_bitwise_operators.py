# programme for assignment operator (task-1)

print('TASK-1')
X=8
Y=10

X+=Y
print('Answer(x+y) =',X)

X=8
Y=10
X-=Y
print('Answer(x-y) =',X)

X=8
Y=10
X*=Y
print('Answer(x*y) =',X)

X=8
Y=10
X/=Y
print('Answer(x/y) =',X)

X=8
Y=10
X%=Y
print('Answer(x%y) =',X)

X=8
Y=10
X^=Y
print('Answer(x^y) =',X)

X=8
Y=10
X<<=Y
print('Answer(x<<y)=',X)

X=8
Y=10
X>>=Y
print('Answer(x>>y) =',X)

X=8
Y=10
X&=Y
print('Answer(x&y) =',X)

X=8
Y=10
X|=Y
print('Answer(x|y) =',X)


# programme for Bitwise operator (TASK-2)

print("TASK-2")
a=int(input('enter 1st number ='))
b=int(input('enter 2nd number ='))

print('Answer (a&b) =',a&b)
print('Answer (a|b) =',a|b)
print('Answer (a^b) =',a^b)
print('Answer (~a) =',~a)
print('Answer (~b)',~b)


# programe for Logical operator (Task-3)

print('Task-3')
m=int(input('enter 1st number ='))
n=int(input('enter 2nd number ='))

z=m<2 and n<3
print('Answer =',z)

v= m<2 or n<3
print('Answer =',v)

q= not(m<2 and n<3)
print('Answer =',q)



