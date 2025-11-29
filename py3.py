def uc (): 
        print("ARİTMETİK OPERATÖRLER")
        a,b=8,3
        top=a+b
        cik=a-b
        cap=a*b
        tambol=a//b
        onbol=a/b
        modal=a%b
        usal=a**b
        print(top)
        print(cik)
        print(cap)
        print(tambol)
        print(onbol)
        print(modal)
        print(usal)
        print("------------------------------")
        c,d=5,3
        print(c,d)
        c+=5
        d=d+3
        print(c,d)
        c*=5
        d=d*3
        print(c,d)
        print("------------------------------")
        tap1=3+5*2
        tap2=(3+5)*2
        print(tap1,tap2)
        print("KARŞILAŞTIRMA OPERATÖRLER")
        a,b,c=2,5,8
        print(a==b)
        print(a==c)
        print(a!=b)
        print(a!=c)
        print(a<b)
        print(a<c)
        print(a>=b)
        print(a>=c)
        print(a<=b)
        print(a<=c)
        print("MANTIKSAL OPERATÖRLER")
        # true and false =>false
        # false and false =>false
        # true and true =>true
        x=True
        y=False
        print(x and y)
        print((3>5)and(5<9))
        print((1<5)and(9>4))
        #or operatöründe bir trafın tru olması yeterli true sonuç için
        print(x or y)
        print((3>5)or(5<9))
        print((1<5)or(9>4))
        print("------------------------------")
        #in operatörü
        a="merhaba"
        b="a"
        c="c"
        print(b in a)
        print(c in a)

        x=[1,2,3,4,5,6,7]
        print(5 in x)
        print("e" in x)
uc()