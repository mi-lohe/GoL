import time
from colorama import init,Fore
import os
from copy import deepcopy
import random
import keyboard 


def TxttoMatrice (Matr) : #injecte le contenu d'un txt. dans une liste booleenne de deux dimensions "X"=true else =false
    with open("C:\\Users\\azertyuiop\\Documents\\GitHub\\TP info\\GoL\\Start.txt",'r') as TxtStart :
        Lines = TxtStart.readlines()
        for indiceLigne in range (len(Lines)):
            for indiceCarac in range(len(Lines[indiceLigne] )):
                Carac = Lines[indiceLigne][indiceCarac]
                if Carac == "X" :
                    Matr[indiceCarac+4][indiceLigne+4] = True
                else :
                    Matr[indiceCarac+4] [indiceLigne+4]= False
    TxtStart.closed

def Vaisseau(modele,x,y): # Fonction chargée de faire apparaitre un vaiseau en mode non randomisé
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
    for g in range (0,HautMatrice):
        for h in range (0,LargMatrice):
            if Matr[h][g] == True:
                print(Fore.BLUE + "██",end="")
            else :
                print(Fore.YELLOW + "██",end="")
        print("")

def AffMatrice2 (Matr):#méthode d'affichage par balayage mais sûre
    for g in range (0,HautMatrice):
        for h in range (0,LargMatrice):
            if Matr[h][g]:
                CursorPos(2*h,g)
                print(Fore.YELLOW+ "██")
            else :
                CursorPos(2*h,g)
                print(Fore.BLUE+ "██") #"██"

def AffMatrice3 (Matr):#méthode d'affiche ultra rapide si peu de cellule , mais rencontre encore des glitchs de supressions
    for g in range (0,HautMatrice):
        for h in range (0,LargMatrice):
            if combVoisin2(Matr,h,g,LargMatrice,HautMatrice,False) > 0 :
                if Matr[h][g] == True:
                    CursorPos((h*2),g)
                    print(Fore.BLUE + "██",end="")
                else :
                    CursorPos((h*2),g)
                    print(Fore.YELLOW +"██",end="")

def AffMatrice4 (Matr,MatrPrec):#méthode d'affiche ultra rapide si peu de cellule 
    for g in range(1,HautMatrice,1):
        for h in range(1,LargMatrice,1):
            if (combVoisin2(Matr,h,g,LargMatrice,HautMatrice,True) > 0 ) or (Matr[h][g] != MatrPrec[h][g]) :
                
                if Matr[h][g] == True:
                    CursorPos((2*h),g)
                    print(Fore.BLUE+"██")
                else :
                    CursorPos((2*h),g)
                    print(Fore.YELLOW+"██")
        #time.sleep(0.1)

def combVoisin(h,m,n):
    return  h[m-1][n-1] + h[m-1][n] + h[m-1][n+1] + h[m][n-1] + h[m][n+1] + h[m+1][n-1] + h[m+1][n] + h[m+1][n+1] 

def combVoisinCentr(h,m,n):
    return  h[m-1][n-1] + h[m-1][n] + h[m-1][n+1] + h[m][n-1] + h[m][n+1] + h[m+1][n-1] + h[m+1][n] + h[m+1][n+1] + h[m][n]

def combVoisin2(h,m,n,mm,nm,CenterInclude):
    s = 0
    for j in range (-1,2,1):
        for i in range(-1,2,1):
            if (h[(m+i) % mm][(n+j) % nm] == True) and (CenterInclude  or not((i == 0) and (j == 0))):
             s = s + 1

    return s

def CalcGoL():
    
    for x in range(0,LargMatrice):
        for y in range(0,HautMatrice):
            
            if (combVoisin2(MemMatrice,x,y,LargMatrice,HautMatrice,False) == 3 ) and (not MemMatrice[x][y]):
                MatriceMonde[x][y] = True
            
            elif( (combVoisin2(MemMatrice,x,y,LargMatrice,HautMatrice,False) == 3) or (combVoisin2(MemMatrice,x,y,LargMatrice,HautMatrice,False) == 2) ) and (MemMatrice[x][y] == True):
                MatriceMonde[x][y] = True
            else : 
                MatriceMonde[x][y] = False
            #time.sleep(0.1)
            #AffMatrice()

init()
LargMatrice = 100
HautMatrice = 50
simActive = "NULL" # ON:Lance la simulation avec un temp fini/OFF:Lance que la première étape/INFINITE:la simulation ne s'arrête jamais 
nbrIteration = 0
ModeChargement = "NULL"
ITERATIONMAX = 400
enPause = False


while (ModeChargement != 'R') and (ModeChargement != 'N') and (ModeChargement != 'T') :
    os.system("cls")
    
    for i in range (int(LargMatrice/2)-20,int(LargMatrice/2)+20) :
        CursorPos(i,8)
        print("─")
    
    CursorPos(int(LargMatrice/2)-22,10)
    print("Mode R : Placement randomisée des cellules")
    CursorPos(int(LargMatrice/2)-22,11)
    print('Mode N : Placement "hard coded" des cellules')
    CursorPos(int(LargMatrice/2)-22,12)
    print("Mode T : Placement des cellules en fonction de Start.txt")
    CursorPos(int(LargMatrice/2)-22,15)
    ModeChargement = input("Réponse (R/N/T) :")
    


while (simActive != 'OFF') and (simActive != 'ON') and (simActive != 'INFINITE') :
    os.system("cls")
    
    for i in range (int(LargMatrice/2)-20,int(LargMatrice/2)+20) :
        CursorPos(i,8)
        print("─")
    
    CursorPos(int(LargMatrice/2)-22,10)
    print("Mode On : On lance le programme avec un nombre d'itérations fini ")
    CursorPos(int(LargMatrice/2)-22,11)
    print('Mode OFF : execute une seule fois la boucle')
    CursorPos(int(LargMatrice/2)-22,12)
    print("Mode INFINITE : Vers 'linfini et l'au dela !")
    CursorPos(int(LargMatrice/2)-22,15)
    simActive = input("Réponse (ON/OFF/INFINITE) :")
    
        
MatriceMonde = [[ False for i in range(HautMatrice)] for j in range(LargMatrice)]

if ModeChargement == "R" : # demande si on commence le jeu avec une partie randomisée ou non 
    MatriceMonde = [[ bool(random.getrandbits(1)) for i in range(HautMatrice)] for j in range(LargMatrice)]
elif ModeChargement == "N":
    MatriceMonde = [[ False for i in range(HautMatrice)] for j in range(LargMatrice)]
elif ModeChargement == "T":
    TxttoMatrice(MatriceMonde) #Injection du txt dans la matrice principale

#initialisation des Matrices : 
MatricePrec = [[ False for i in range(HautMatrice)] for j in range(LargMatrice)]

MemMatrice = deepcopy(MatriceMonde)


if ModeChargement == 'N':
    Vaisseau ("planneur", 4,40)
    #Vaisseau ("LWSS",15,30)
    #"Vaisseau ("point",25,20)
    #Vaisseau ("LWSS",15,10)

#Creation d'une matrice à  n-1 étape et inversé pour forcer la MAJ complète de l'écran 
for y in range(0,HautMatrice):
    for x in range(0,LargMatrice):
        MatricePrec[x][y] = not MatriceMonde[x][y]


#AffMatrice4(MatriceMonde,MatricePrec)
AffMatrice4(MatriceMonde,MatricePrec)
#AffMatrice2(MatriceMonde)
while (simActive == "ON") or (simActive == "INFINITE"): #Boucle principale 
    #time.sleep(1)
    
    nbrIteration += 1

    if (nbrIteration >= ITERATIONMAX) and (simActive == "ON")  :
        simActive = "OFF" 
    
    if keyboard.is_pressed('q'):
        simActive = "OFF"

    if keyboard.is_pressed('p'):
        enPause = True

    if keyboard.is_pressed('r'):
        enPause = False
    
    if enPause == False :
       
        MatricePrec = deepcopy(MatriceMonde)
        MemMatrice = deepcopy(MatriceMonde)

        CalcGoL()
        #AffMatrice2(MatriceMonde)
        AffMatrice4(MatriceMonde,MatricePrec)

os.system("cls")
print("GOODBYE")
time.sleep(1)
os.system("cls")
    
    
    
    
    
    

        
    
     
    







