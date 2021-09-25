from math  import gcd #include<math.h> pow(a,b)
from random import choice #a[a,b,c] choice(a)

##void asdasd(){
# asdasdsd
# }



def isPrime(num): 
    if num < 2: return False
    if num == 2: return True

##for(int i=2,i<=num/2,i++)
    for i in range(2, (num//2) +1):
        if num % i == 0: return False

    return True

def euler(p, q):
    return (p - 1)*(q - 1)

def selectd(num):
    listd = []
    for i in range(2, num):
        if gcd(i, num) == 1 and isPrime(i):
            listd.append(i)
    return listd

def finde(d, eul):
    e = 0
    while (e*d - 1) % eul != 0 or e==d:
        e += 1
    return e

def process(msg, key):
    out = ""
    msg=msg.lower()##minusculas
    for c in msg:##sadsdaas c=s c=a c=d
        if c == ' ': 
            out += '32 '  
        else:
            n = ord(c) - ord('a') ##ascii(c)0
            res = (n**key[1]) % key[0]##n=M key[1]=e key[0]=n
            out += str(res)+' '##amsq 0 12 18 16
    return out

def process1(msg, key):##0 12 18 16
    out = ""
    
    for c in msg:
        if c == ord(' '): 
            out += ' '
        else:
            res = (c**key[1]) % key[0]
            out += chr(res+ord('a'))

    
    return out ##amigo

def outword(msg): ##08 45 65 92 
    out = ""
    
    for c in msg:
        if c == 32: 
            out += '  '
        elif (c >= 0) and (c <= 25): 
            out += chr(c+ord('a'))+' '
        else:
            out+=str(c)+' '

    
    return out #g 45 65 92


if __name__ == "__main__":
    op = int(input("Encriptar(1) o desencriptar(2)"))
    key_public = [0, 0]
    key_private = [0, 0]
    arrWord=[]
    arrWord1=[]
    p = q = 10


    if op == 1:
        while not isPrime(p) or not isPrime(q):
            p = int(input("Ingrese p: "))
            q = int(input("Ingrese q: "))

        n = p*q
        eul = euler(p,q)
        d = choice(selectd(eul))
        e = finde(d, eul)

        key_public = [n, e]
        key_private = [n, d]

        #print(f"Public: {key_public}")
        #print(f"Private: {key_private}")
        msg = input("Escriba la palabra: ")

    elif op == 2:
        prompt = "Ingrese la clave privada: " 
        key_private = [int(x) for x in input(prompt).split()]## 22 8 separa los espacios key_private[0,0],luego[22,8]
        



    if op == 1:
        # encriptar
        f = open ('Archivo.txt','w')
        f.write(process(msg, key_public))
        f.close()
        arrWord1=[int(x) for x in process(msg, key_public).split()]##08 02 01 46 arrqord[08,02,01,46]
        #print(f"Encriptado: {outword(arrWord1)}")

    elif op == 2:
        # desencriptar
        f = open ('Archivo.txt','r')##05 65 49 85
        mensaje = f.read()
        arrWord=[int(x) for x in mensaje.split()]
        f.close()
        #print(f"Desencriptado: {process1(arrWord, key_private)}")
