from random import sample
dic = {
'¿De qué color es el caballo blanco de Santiago?': ['Blanco','Negro','Marrón'],
'En este banco hay sentado un padre y un hijo, el Padre se llama Juan, el hijo, ya te lo he dicho': ['Elías','Miguel','Esteban'],
'Oro parece, plata no es': ['Piña','Pera','Plátano'],
}
n=-1
spek=0
sol = {
'¿De qué color es el caballo blanco de Santiago?': 'a',
'En este banco hay sentado un padre y un hijo, el Padre se llama Juan, el hijo, ya te lo he dicho': 'c',
'Oro parece, plata no es': 'c',
}
for i in sample(list(dic.items()),2):
    q=str(i).split("', ")[0]
    q=q.replace('(\'','')
    print (q)
    pa = dic[q]
    print ('a - ' + pa[0])
    print ('b - ' + pa[1])
    print ('c - ' + pa[2])
    pec = input()
    if pec != sol [q]: 
        print('Error')
        spek = spek-5
    else:
        print('Acierto')
        spek = spek+10
print('Puntuación: '+ str(spek))