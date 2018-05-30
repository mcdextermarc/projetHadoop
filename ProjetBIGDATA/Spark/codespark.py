#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
start_time = time.time()
from pyspark import SparkContext  
sc=SparkContext()

rdd1=sc.textFile('text.txt')
graph=rdd1.map(lambda x:x.split()).map(lambda x:(x[0],[float(x[2]),x[1]]))
sommet=graph.keys().distinct().collect()
noeudsource=sommet.pop(0)

def f(x):
     if x[0]==noeudsource:
       return (float(x[1][0]),(noeudsource,x[1][1]))
     else:
       return (float("inf"),(None,x[1][1]))


dijkstra=graph.map(f).distinct().collect()
graph=graph.groupByKey().map(lambda x:(x[0],list(x[1])))

while len(sommet)!=0:
      L1=[]
      L2=[]
      noeudist=sc.parallelize(dijkstra).filter(lambda x:x[1][1] in sommet).min()
      distmin=noeudist[0]
      noeudelu=noeudist[1][1]
      del(sommet[sommet.index(noeudelu)])
      success=graph.filter(lambda x : x[0]==noeudelu).flatMap(lambda x:x[1]).flatMap(lambda x: x).collect()
      L1=[x for x in success if (success.index(x)%2==0)]
      L2=[x for x in success if (success.index(x)%2==1)]
      if len(L2)!=0 :
         for noeud in L2:
             for i in range(len(dijkstra)):
                 if dijkstra[i][1][1]==noeud and noeud in sommet:
                    if dijkstra[i][0]>L1[L2.index(noeud)]+distmin: 
                       dijkstra[i]=(L1[L2.index(noeud)]+distmin,(noeudelu,dijkstra[i][1][1]))

dijkstra

print("Temps d execution : %s secondes ---" % (time.time() - start_time))

  
#final=sc.parallelize(dijkstra)
#final.saveAsTextFile('/home/dexter/output')
#final.coalesce(1).saveAsTextFile("/home/dexter/output")


