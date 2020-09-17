





def Vaisseau(modele,x,y,r): # Fonction chargée de faire apparaitre un vaiseau en mode non randomisé
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