# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:19:33 2021

@author: Ye Jian_cheng
"""

class Node(object):           #classe nodo
    def __init__(self, value):   #costruttore e variabile che si passano
        self.value = value
        self.left = None
        self.right= None 
        
class BinaryTree(object):
    def __init__(self,root):
        self.root= Node(root)   #in questa classe binary usa i node, in quanto sono eleemnti che costituiscono
    
    
    
    
    
    
    #attraversamento : FANUZIONA , COPIA E BASTA DIO CANE1!! 
    def preOrder(self,start,traversal): #visita figli e poi figli dei figli    #travelsl èuna stringa che contiene ordine in cui visita
        
        if start:    #vuold dire start!= none 
             traversal+= (str(start.value)+"-")
             
             traversal= self.preOrder(start.left,traversal)   #richiama ricorsiva
             traversal= self.preOrder(start.right,traversal)
        
        return traversal #ritorno ordine che contiene il persorco dei traversal
      
    
    def inorder(self, start, traversal):
        
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal
    
    def postOrder(self, start, traversal):
        
        if start !=None:
            traversal = self.postOrder(start.left, traversal)
            traversal = self.postOrder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


    
    
    
        


n1=Node(1)
print("print prova nodo ",n1.value)

#   1
# 2   3
#4 5 6  7


tree = BinaryTree(1) #albero con 1 in root
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left = Node(4)
tree.root.left.right= Node(5)
tree.root.right.left= Node(6)
tree.root.right.right=Node(7)

ris=tree.preOrder(tree.root,"")
print("ordine  visit",ris)











