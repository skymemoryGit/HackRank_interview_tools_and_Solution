

def truckTour(petrolpumps):
    
    for i in range(len(petrolpumps)):
        elemento1=petrolpumps[1]
        p=elemento1[0]
        d=elemento1[1]
        
        lista=shift(petrolpumps,-i)
        print(lista)
        
        
        
        
        ris=IsvalidStart(p,d,lista)
        print(ris)
    
    
    
def shift(seq, n):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]
   
    
def IsvalidStart(pumps,distance,arr):
    if(pumps-distance<0):
        return False
        
    sommaDistanze=0
    sommaPumps=0
    
    for i in range(len(arr)):
        print(arr)
        sommaPumps=sommaPumps+arr[i][0]
        sommaDistanze=sommaDistanze+arr[i][1]
        print(sommaPumps)
        print(sommaDistanze)
    if(sommaDistanze>sommaPumps):
        return True
    else:
        return False
     
    
        

ls=[[1,7],[10,3],[4,3]]








