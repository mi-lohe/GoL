import time
import colorama
import os
from copy import deepcopy


LargMatrice = 40
HautMatrice = 40
simActive = True 
nbrIteration = 0

MatriceMonde = [[ False for i in range(LargMatrice)] for j in range(HautMatrice)]
MemMatrice = MatriceMonde[:]

MatriceMonde[9][5] = True
MatriceMonde[9][6] = True
MatriceMonde[9][7] = True



def AffMatrice ():
    os.system('cls')
    for g in range (HautMatrice):
        for h in range (LargMatrice):
            if MatriceMonde[h][g]:
                print("██",end="")
            else :
                print("░░",end="")
        print("")
        

def AffDebug():
    AffMatrice()
    for g in range (1,HautMatrice-1):
        for h in range (LargMatrice-1):
            print(combVoisin(MemMatrice,h,g)," ",end="")
        print("")

def combVoisin(h,m,n):
    return  h[m-1][n-1] + h[m-1][n] + h[m-1][n+1] + h[m][n-1] + h[m][n+1] + h[m+1][n-1] + h[m+1][n] + h[m+1][n+1] 


while simActive:
    time.sleep(0.2)
    
    nbrIteration += 1
    print("nop", nbrIteration,combVoisin(MatriceMonde,6,5))
    if nbrIteration >= 30:
        simActive = False 
    
    MemMatrice = deepcopy(MatriceMonde)
    #AffDebug()
    AffMatrice()

    print("NbrIteration", nbrIteration,combVoisin(MatriceMonde,4,5))
    
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
    
    
    

        
    
     
    







