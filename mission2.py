import numpy as np
from test import read

'''
Mission 2 par encore terminé
Code fonctionnant sur base du 'Hammings Code'
'''

def Number_ParityBits(m):
    for i in range(m):
        if(2**i >= m+i+1):
            return i

def possible_Parity(data, r):
    j=0
    k=1
    m=len(data)
    res=''
    for i in range(1, m+r+1):
        if (i== 2**j):
            res=res+'0'
            j+=1
        else:
            res=res+str(data[-1*k])
            k+=1
    return res[::-1]

def Calcul_Parity(arr, r):
    n=len(arr)
    liste_Parity=[]
    for i in range(r):
        val=0
        for j in range(1, n+1):
            if (j& (2**i) == (2**i)):
                val= val ^ int(arr[-1*j])
        liste_Parity.append(int(val))
    return liste_Parity

def detect_Error(arr, nr):
    n=len(arr)
    res=0
    for i in range(nr):
        val=0
        for j in range(1, n+1):
            if(j& (2**i)==(2**i)):
                val=val ^ int(arr[-1*j])
    return int(str(res), 2)

def cut(data):
    liste=[]
    n=0
    tup=[]
    for i in data:
        if n <4:
            tup.append(int(i))
            n+=1
        if n ==4:
            liste.append(tup)
            tup=[]
            n=0
    #ata)!=0:
    #n(data)
    #%4 != 0:
    #del data[:len(data)-x%4]
    #liste.append(data)
    return liste

def odd_even(number):
    if number%2 == 0:
        return '0'
    else:
        return '1'

def verification(codes):
    code=list(np.array(codes).reshape(-1,))
    P1=code[3]+code[2]+code[0]
    P2=code[3]+code[1]+code[0]
    P3=code[2]+code[1]+code[0]

    binary='0b'+odd_even(P3)+odd_even(P2)+odd_even(P1)
    return int(binary)

    

def correction(code, change):
    z=0
    output=''
    if change == None:
        while z < 4:
            output+=str(code[0][z])
            z+=1
        return output
    else:
        while z < len(code)-3:
            if code[0][z]==change:
                if code[0][z]==0:
                    code[0][z]=1
                else:
                    code[0][z]=0
            output+=str(code[z])
            z+=1
    return output


#D7 : D6 : D5 : P4 : D3 : P2 : P1  [1 0 1 1 1 0 0]
#si pair -> 1
#si impaire -> 0

data='1011'
m=len(data)
datas=list(data)
liste_Parity=cut(datas)
for i in liste_Parity:
    r=Number_ParityBits(len(i))
    arr=possible_Parity(i, r)
    Parity=Calcul_Parity(arr, r)
    for z  in Parity:
        i.append(z)
final=np.array(liste_Parity)
#print(final)
matrix_modified=np.array([[1,0,1,1,1,0,0]])
matrix_util=np.array([[1,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,1,1,0,0,1]])

#Recepteur
#---------------
correcti=[]
z=0
jsp=0
while z <3:
    for x in range(matrix_modified.shape[1]-1):
        result=matrix_modified[0][x]*matrix_util[z][x]
        jsp=result+jsp
    if jsp%2 == 0:
        correcti.append(1)
    else:
        correcti.append(0)
    z+=1
    jsp=0
    result=0
print(correcti)