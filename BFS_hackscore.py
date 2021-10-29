#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    graph=creagraph(n,edges)    #è un dizionario
     
    
    print(graph)
    visited=[]
    level=level_bfs(visited, graph, s)    # function callin
    print("\nlevel of nodes",level)
    
    ris=[]
    for i in range (1,len(level.keys())+1):
        #print(level.keys())
        
        if(i in level.keys()):
            if(level[i]==-1):
                ris.append(-1)
            else:
                ris.append(level[i]*6)
            
        
        
    ris.remove(0)
    print(ris)
    return ris
      
    
    
    
def creagraph(n,edges):
    g={}
    for i in range(1,n+1):
        ls=[]
        g[i]=ls   #init chiavi
    
    
    for k in range(1,n+1):
        ls_i=[]
        #print("per nodo ",k)
        for i in edges:
            #print()
            #print(i[0])
            #print("k",k)
            
            
            if(i[0]==k):
                #print("passato")
                ls_i.append(i[1])
                #print(i[1])
            if(i[1]==k):        #aggiugni anche all'altro nodo
                ls_i.append(i[0])
        ls_i_unique=list(set(ls_i))
        g[k]=ls_i_unique
        #print(ls_i)
        
       # print("____")
        
       
       
        
   # print(g)
    return g   
        
    


def bfs_v(visited, graph, node): #function for BFS
    
  
  
  visited = [] # List for visited nodes.
  queue = []     #Initialize a queue
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def level_bfs(visited, graph, node): #function for BFS
    
  lv=0
  
  diz_lv={}    
  
  visited = [] # List for visited nodes.
  queue = []     #Initialize a queue
  visited.append(node)
  queue.append(node)
  
  
  diz_lv[node]=lv
  lv=lv+1    #+1 perchè messo start node in visited e incremento lv
  
  #print("queue ",queue)
  while queue:          # Creating loop to visit each node
    #print("queue in while ",queue)
    m = queue.pop(0) 
    #ls_lv.append(lv)
    #print("rimosso dalla coda",m)

    
    
    for neighbour in graph[m]:
        
        
        #print("vicini:", graph[m])
        #print("diz attuale dei lv ", diz_lv)
        
        if neighbour not in visited:
        
        
        
            visited.append(neighbour)
            queue.append(neighbour)
            
            
            
            diz_lv[neighbour]=diz_lv[m]+1   #!!!! IDEA : ANZICHE USARE CONTATORE, PRENDI LV DEL PADRE E AGGIUGNI UNO! 
        
        
       
    
    
    #completamento: aggiungo -1 per i nodi non connessi
  lista_tutti=list(graph.keys())
  lista_nodiconnessi=list(diz_lv.keys())
  lista_diff=set(lista_tutti).difference(lista_nodiconnessi)
  

  
  
  print("connessi",lista_nodiconnessi)
  print("tutti ",lista_tutti)
  print("diff",lista_diff)
  for i in lista_diff:
      diz_lv[i]=-1
        
    
   
  #print("diz level ",diz_lv)
  return diz_lv

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
