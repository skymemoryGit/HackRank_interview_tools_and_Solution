

def palindromeIndex(s):
    index= -1
    length=len(s)
    
    for i in range(0,int(length/2)):
        if (s[i]!=s[length-1-i]): #trovato dis-matching
            
            print("dismaching")
            if( i+1<length):
                
                substring= s[i+1:length-i]
                print("sub: "+substring)
                ris=isRightStringValidPalindrome(substring)
                if(ris==True):
                    return i
                else:
                    return length-1-i
    
    return index # non trova dismathing , quindi è gia palindromo

def isRightStringValidPalindrome(s):  #checa palidnromo
                                        #metodo di check palidnormo triviale
    lenght=len(s)
    
    
    for i in range(0,int(lenght/2)):  
        #print(int(lenght/2))
        #print(lenght)
        #print(lenght/2)
        if(s[i]!=s[lenght-1-i ]):
          
            return False
    return True


s="madafm"
ris=palindromeIndex(s)
print(ris)




        
            
