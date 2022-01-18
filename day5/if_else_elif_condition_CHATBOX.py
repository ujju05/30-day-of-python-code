
# programe for if else condition (TASK-1)

A=int(input('enter 1st number ='))
B=2

if (A%B==0):
    print('Value is Even')

else:
    print('Value is odd')

# programe for if-else-elif condition (TASK-2)

P=int(input('enter your percentage ='))

if (P>=70):
    print ('Dist')

elif (P>=60 and P<=70):
    print('Congratulations,you passed in 1st Division')

elif (P>=50 and P<=60):
    print('Congratulations,you passed in 2nd Division')         

elif (P>=40 and P<=50):
    print('Congratulations, you passed in 3rd Division')

else:
    print('you have failed,Try Next Time')


# programe for chat-Box

# programe for chat-Box

A=""
while A!='bye':
    print()
    A=input('Enter your message =')
    

    if (A=="hello" or A=="HELLO"):
        print('Hello SIR/MAM')

    elif (A=="how do you do ?" or A=='how are you ?'):
         print("I AM FINE")

    elif (A=="what is your name ?" or A=="please tell me your name " or A=="tell me your owner name " ):
         print('MY NAME IS python')

    elif (A=="who is your owner ?" or A=="tell me your owner name" or A=="please tell me your owner name"): 
         print('my owner name is "Guido Van Rossum"')

    elif (A=="who is your best friend ?" or A=="tell me your best friend name " or A=='please tell me your best friend name'):
        print ('MY BEST FRIEND NAME IS "programmer"')

    elif(A=="bye"):
        print('BYE')                  

    else:
        print('sorry')

print('bye')









