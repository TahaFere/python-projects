def bes ():
        print("delta hesaplama")
        x,y,z=map(int,input("lütfen aralara virgül koyarak a,b,c değer giriniz:").split(","))
        #a=int(input("1. sayıyı giriniz:"))
        #b=int(input("2. sayıyı giriniz:"))
        #c=int(input("3. sayıyı giriniz:"))
        delta=(y**2)-(4*x*z)
        print("delta sonucu sıfırdan büyük mü? =>",delta>0 )

        print("VİZE-FİNAL hesaplama")
        vize=int(input("vize notunuzu giriniz:"))
        final=int(input("final notunuzu giriniz:"))
        vize=vize*4/10
        final=final*6/10
        #print("ders ortlamanız:",vize+final,"\nvize notunuz:",vize,"\nfinal notunuz:",final,"\ndersi geçtiniz:",(vize+final)>60)
        print("ders ortalmanız:{}, vize notunzu:{}, final notunuz:{}, dersi geçme:{}".format(vize+final,vize,final,(vize+final)>60))

        print("DAİRE ALAN-ÇEVRE HESAPLAMA")
        yaricap=int(input("yarıçapı giriniz:"))
        pi=3.14
        dairealan=pi*yaricap**2
        dairecevre=2*pi*yaricap
        print("dairenin yarıçapı:",yaricap,"\ndairenin alanı:",dairealan,"\ndairenin çevresi:",dairecevre)
bes()