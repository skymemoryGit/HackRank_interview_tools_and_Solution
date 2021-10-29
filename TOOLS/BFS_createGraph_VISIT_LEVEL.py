# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:24:35 2021

@author: Ye Jian_cheng
"""


def bfs(n, m, edges, s): #test
    # Write your code here
    graph=creagraph(n,edges)    #è un dizionario
    
    graph_Test={1: [8, 10, 3], 2: [5], 3: [1], 4: [], 5: [2], 6: [], 7: [], 8: [1], 9: [], 10: [1]}
    print(graph_Test)

    
    #print(graph)
    
    # Driver Code
    print("Following is the Breadth-First Search")
    
    visited=[]
    #bfs_v(visited, graph, 1) 
    
    level=level_bfs(visited, graph_Test, 3)    # function callin
    print("\nlevel of nodes",level)
    
    




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
        g[k]=ls_i
        #print(ls_i)
        
       # print("____")
        
       
       
        
   # print(g)
    return g   
        
    


def bfs_v(visited, graph, node): #function for BFS attraversamento
    
  
  
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
        
        
   #fino qui ho diz dei nodi connessi con i loro livelli di profondita    
    
    
  #lo completamento: aggiungo -1 per i nodi non connessi
  lista_tutti=list(graph.keys())
  lista_nodiconnessi=list(diz_lv.keys())
  lista_diff=set(lista_tutti).difference(lista_nodiconnessi)    # e' una specie di Xor
  

  
  
  print("connessi",lista_nodiconnessi)
  print("tutti ",lista_tutti)
  print("diff",lista_diff)
  for i in lista_diff:
      diz_lv[i]=-1
  
    
   
  #print("diz level ",diz_lv)
  return diz_lv

    
#####################################
#main

n=8  #numerati da 1-8
m=7
edges=[[1,2],[1,4],[2,3],[4,6],[6,7],[3,7],[6,8]]
bfs(n,m,edges,5)
