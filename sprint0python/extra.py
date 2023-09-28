from random import choice
e=True
while e:
    print ('Escoge el nivel de dificultad')
    print ('1- Fácil')
    print ('2- Normal')
    print ('3- Difícil')
    dif = int(input())
    def trl (dif):
        if dif==1:
            return ('Facil')
        elif dif==2:
            return ('Normal')
        return ('Dificil')
    i=trl(dif)
    with open ("palabras.txt","r") as r:
        sw=r.read().splitlines()
        sw=choice(sw [sw.index(i):(sw.index(i)+3)])
    rw=''
    tl=''
    for i in range(len(sw)):
        rw=rw+'_'
    print(rw)
    m=0
    while m<6 and rw!=sw:
        tw=''
        l=input('Prueba una letra\n')
        for i in range(len(sw)):
            if l==sw [i]:
                tw+=l
                e=False
            else:
                tw+=rw[i]
                e=True
        rw=tw
        tl+=l+' '
        if e:
            m+=1
        print (rw)
        print ('Errores (Máximo 6): '+str(m))
        print ('Letras probadas: '+tl)
    if m>=6:
       print ('Has perdido, la palabra era: '+sw)
    else:
        print ('Has ganado, la palabra era: '+sw)
    if input('¿Volver a jugar? s/n')=='s':
        e=True
    else:
        e=False