def funkeypress():
    
    import msvcrt
    while 1:
        if msvcrt.kbhit():                 
            a = ord(msvcrt.getch())         
            if a == 0 or a == 224:         
                b = ord(msvcrt.getch())    
                x = a + (b*256)             
                return x                    
            else:
                return a                    



def printMatriz(matriz):
        a = ""
        for x in range(20):
            for y in range(70):
                a = a + matriz[x][y]
            
            a = a + "\n"
        print "\n" * 20
        print a


       


if __name__ == '__main__':
    
    matriz = [None] * 20
    for x in range(20):
        matriz[x] = [' '] * 70
    i = 0
    j = 0
    while 1:
       
        x = funkeypress()
       
        if x in map(ord,'aA'):                      
            print "press A"
            matriz[i][j] = "*"
            if j > 0:
                j = j - 1
            printMatriz(matriz)
           

        if x in map(ord,'dD'):                     
            matriz[i][j] = "*"
            if j < 69:
                j = j + 1
            printMatriz(matriz)
            
    
        if x in map(ord,'wW'):                      
            matriz[i][j] = "*"
            if i > 0:
                i = i - 1 
            printMatriz(matriz)
        
        if x in map(ord,'sS'):                     
            matriz[i][j] = "*"
            if i < 19:
                i = i + 1
            printMatriz(matriz)
       
