from random import randrange
n=0
def trl (tek):
    match tek:
        case 1: return ('piedra')
        case 2: return ('papel')
        case 3: return ('tijera')
def ppt (mec,pec):
    if (mec==pec-1 and mec<3) or (mec==3 and pec==1):
        print ('Has perdido, '+trl(pec)+' gana a '+trl(mec))
        return (-1)
    elif mec==pec:
        print ('Has empatado')
        return(0)
    else:
        print ('Has ganado, '+trl(mec)+' gana a '+trl(pec))
        return (1)
for i in range (5):
    mec=int (input('¿Piedra, papel o tijera? 1/2/3\n'))
    pec= randrange(1,4)
    print (trl(pec))
    n=n + ppt (mec,pec)
print (n)
if n>0:
    print ('Has ganado')
elif n<0:
    print ('Has perdido')
else:
    print ('Has empatado')