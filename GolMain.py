import time
from colorama import init,Fore
import os
from copy import deepcopy
import random


init()
LargMatrice = 100
HautMatrice = 50
simActive = "INFINITE" # ON:Lance la simulation avec un temp fini/OFF:Lance que la première étape/INFINITE:la simulation ne s'arrête jamais 
nbrIteration = 0
blyat=0
ITERATIONMAX = 400

TxtStart = open("C:\\Users\\azertyuiop\\Documents\\GitHub\\TP info\\GoL\\Start.txt")
Lines = TxtStart.readlines()
for Line in Lines:
    print(Line)

Randomisation = input("Random ?")




if Randomisation == "Y" : # demande si on commence le jeu avec une partie randomisée ou non 
    MatriceMonde = [[ bool(random.getrandbits(1)) for i in range(HautMatrice)] for j in range(LargMatrice)]
else:
    MatriceMonde = [[ False for i in range(HautMatrice)] for j in range(LargMatrice)]

MemMatrice = deepcopy(MatriceMonde)
MatricePrec = [[ False for i in range(HautMatrice)] for j in range(LargMatrice)]

for y in range(0,HautMatrice):
    for x in range(0,LargMatrice):
        MatricePrec[x][y] = not MatriceMonde[x][y]

def Vaisseau(modele,x,y): # Fonction chargée de faire apparaitre un vaiseau en mode non randomisé
    if Randomisation != 'Y':
        if modele == "planneur" : 

            MatriceMonde[x][y] = True
            MatriceMonde[x+1][y] = True
            MatriceMonde[x+2][y] = True
            MatriceMonde[x+2][y+1] = True
            MatriceMonde[x+1][y+2] = True
        elif modele == "LWSS" :
            MatriceMonde[x][y+1] = True
            MatriceMonde[x][y+3] = True
            MatriceMonde[x+1][y] = True
            MatriceMonde[x+2][y] = True
            MatriceMonde[x+3][y] = True
            MatriceMonde[x+3][y+3] = True
            MatriceMonde[x+4][y] = True
            MatriceMonde[x+4][y+1] = True
            MatriceMonde[x+4][y+2] = True
        elif modele == "point":
            MatriceMonde[x][y]=True
        elif modele == "oscilateur 2P":
            MatriceMonde[x][y] = True
            MatriceMonde[x][y+1] = True
            MatriceMonde[x][y+2] = True


def CursorPos(x,y): #Place le curseur sur une position x , y spécifié
    print("\x1b["+str(y)+";"+str(x)+"H",end="")


def AffMatrice1 (Matr): #méthode d'affichage lente et obsolète
    os.system("cls")
    for g in range (1,HautMatrice):
        for h in range (1,LargMatrice):
            if Matr[h][g] == True:
                print(Fore.BLUE + "██",end="")
            else :
                print(Fore.YELLOW + "██",end="")
        print("")
        
def AffMatrice2 (Matr):#méthode d'affichage par balayage mais sûre
    for g in range (1,HautMatrice-1):
        for h in range (1,LargMatrice-1):
            if Matr[h][g]:
                CursorPos(2*h,g)
                print(Fore.BLUE + "██")
            else :
                CursorPos(2*h,g)
                print(Fore.YELLOW +"██")

def AffMatrice3 (Matr):#méthode d'affiche ultra rapide si peu de cellule , mais rencontre encore des glitchs de supressions
    for g in range (1,HautMatrice-1):
        for h in range (1,LargMatrice-1):
            if combVoisin2(Matr,h,g) > 0 :
                if Matr[h][g] == True:
                    CursorPos((h*2),g)
                    print(Fore.BLUE + "██")
                else :
                    CursorPos((h*2),g)
                    print(Fore.YELLOW +"██")

def AffMatrice4 (Matr):#méthode d'affiche ultra rapide si peu de cellule 
    for g in range (1,HautMatrice-1):
        for h in range (1,LargMatrice-1):
            if (combVoisin(Matr,h,g) > 0 ) or (MatriceMonde[h][g] != MatricePrec[h][g]) :
                if Matr[h][g] == True:
                    CursorPos((h*2),g)
                    print(Fore.BLUE + "██")
                else :
                    CursorPos((h*2),g)
                    print(Fore.YELLOW +"██")

def AffDebug(Matr):
    AffMatrice4(Matr)
    for g in range (1,HautMatrice-1):
        for h in range (LargMatrice-1):
            print(combVoisin(MemMatrice,h,g)," ",end="")
        print("")

def combVoisin(h,m,n):
    return  h[m-1][n-1] + h[m-1][n] + h[m-1][n+1] + h[m][n-1] + h[m][n+1] + h[m+1][n-1] + h[m+1][n] + h[m+1][n+1] 

def combVoisin2(h,m,n):
    return  h[m-1][n-1] + h[m-1][n] + h[m-1][n+1] + h[m][n-1] + h[m][n+1] + h[m+1][n-1] + h[m+1][n] + h[m+1][n+1] + h[m][n]


#Vaisseau ("planneur", 4,40)
Vaisseau ("LWSS",15,30)
Vaisseau ("point",25,20)
Vaisseau ("LWSS",15,10)
AffMatrice4(MatriceMonde)
while simActive == "ON" or simActive == "INFINITE":
    #time.sleep(1)
    
    nbrIteration += 1
    #print("nop", nbrIteration,combVoisin(MatriceMonde,6,5))
    if (nbrIteration >= ITERATIONMAX) and (simActive == "ON")  :
        simActive = "OFF" 
    
    MemMatrice = deepcopy(MatriceMonde)
    #AffDebug()

    
    #print("NbrIteration", nbrIteration,combVoisin(MatriceMonde,4,5))
    
    
    MatricePrec = deepcopy(MatriceMonde)
    for x in range (1,LargMatrice-1):
        for y in range(1,HautMatrice-1):
            
            if (combVoisin(MemMatrice,x,y) == 3 ) and (not MemMatrice[x][y]):
                MatriceMonde[x][y] = True
            
            elif(((combVoisin(MemMatrice,x,y) == 3) or (combVoisin(MemMatrice,x,y) == 2) )) and MemMatrice[x][y]:
                MatriceMonde[x][y] = True
            else : 
                MatriceMonde[x][y] = False
               #time.sleep(0.1)
            #AffMatrice()
    AffMatrice4(MatriceMonde)
    
    
    
    
    
    

        
    
     
    







