#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:13:35 2018

@author: dexter
"""
import time
import math
import sys
start_time = time.time()
noeudencour = None
#noeud_source=sys.argv[1]
graphvois = {}
graph={}
L=[]
noeudelu=None
itineraire=""
way=' '
#doc=open('/home/dexter/text.txt')
for line in sys.stdin:
	line = line.strip('\n').split(' ')
	noeud = line[0]
	successeur = line[1]
	distance = int(line[2])
	if noeudencour != None:
           if noeudencour != noeud:
                 if len(graphvois.keys())!= 0:
                   #print(graphvois)
                   graph[noeudencour]=graphvois
                 graphvois={}
                 graphvois[successeur]=distance
                 noeudencour = noeud
                 distance=0
           else:
                graphvois[successeur]=distance
                    
	else:
	      noeudencour = noeud
	      graphvois[successeur]=distance
graph[noeudencour]=graphvois                
#print(graph)
sommet=list(graph.keys())
noeud_source=sommet.pop(0)
def chemin(noeud1):
    global way
    for item in L:
        if item[0]==noeud1:
            way=item[1]+' '+way
            if item[1]!=noeud_source:
                chemin(item[1])
            else :
                way=noeud_source+way
    return way               
                
        
for noeud in sommet:
    if noeud in graph[noeud_source].keys():
        L.append([noeud,noeud_source,graph[noeud_source][noeud]])
    else:
        L.append([noeud,None,math.inf])
   
while len(sommet)!=0:
    distmin=math.inf
    for i in range(len(L)):
        if L[i][2]<=distmin and (L[i][0] in sommet): 
            distmin=L[i][2]
            noeudelu=L[i][0]
            indice=i
    itineraire=str(chemin(noeudelu))
    print(itineraire[1:]+noeudelu+' '+str(L[indice][2]))
    way=' '
    #print(L) 
    del(sommet[sommet.index(noeudelu)])
    if len(graph[noeudelu].keys())!=0 :
       for noeud in graph[noeudelu].keys():
           for i in range(len(L)):
               if L[i][0]==noeud and noeud in sommet:
                  if L[i][2]>=graph[noeudelu][noeud]+distmin: 
                     L[i][2]=graph[noeudelu][noeud]+distmin 
                     L[i][1]=noeudelu

    # Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))            
               
