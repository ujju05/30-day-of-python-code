# programe for give discount on product
num=''
while num!="you enter wrong code ":
        print('a.= Iphone 11 ') 
        print('b.= Iphone 12') 
        print('c.= Iphone 13') 
        print('d.= Laptop ') 
        print('e.= Sony LCD ')


        x=input('enter your product alphabet =')

        if (x=='a'):
            print('you select Iphone 11 = 79,999')

        elif (x=='b'):
            print('you select Iphone 12 = 44,999')

        elif (x=='c'):
            print('you select Iphone 13 = 1,20,000')

        elif (x=='d'):
            print('you select Laptop = 45000')

        elif (x=='e'):
            print('you select Sony LCD = 49,999')

        else:
            print('you enter wrong alphabet')

        m="PRO20"
        print('if you have coupon code you will get 20% discount')
        u=input('Enter coupon code =')

        g=str(input('Enter Again your product alphabet = '))
        
        a=79999
        b=44999
        c=120000
        d=45999
        e=49999
        if (u==m):
            if(g=="a"):
                w=a*20//100
                v=a-w
                print('You Pay =',v)

            elif(g=='b'):
                w=b*20//100
                v=b-w
                print('You Pay =',v)

            elif(g=='c'):
                w=c*20//100
                v=c-w
                print('You Pay =',v)

            elif(g=="d"):
                w=d*20//100
                v=d-w
                print('You Pay =',v)

            elif(g=="e"):
                w=e*20//100
                v=e-w
                print('You Pay =',v)

            else:
                print('you enter wrong alphabet,please Try Next time')     

        else:
             print('you enter wrong coupon code,you willnot give a discount',)


print('Try Next Time')



