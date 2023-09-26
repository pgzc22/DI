dic = {
'¿De qué color es el caballo blanco de Santiago?': ['Blanco','Negro','Marrón'],
'En este banco hay sentado un padre y un hijo, el Padre se llama Juan, el hijo, ya te lo he dicho': ['Elías','Miguel','Esteban'],
'Oro parece, plata no es': ['Piña','Pera','Plátano'],
}
n=-1
spek=0
mec = ['a','c','c']
for i in dic:
    n=n+1
    print (i)
    pa = dic[i]
    print ('a - ' + pa[0])
    print ('b - ' + pa[1])
    print ('c - ' + pa[2])
    pec = input()
    if pec != mec [n]: 
        print('Error')
        spek = spek-5
    else:
        print('Acierto')
        spek = spek+10
print('Puntuación: '+ str(spek))