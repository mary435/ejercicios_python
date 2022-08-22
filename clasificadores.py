#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:40:31 2021

@author: marilinaorihuela
"""

#%%
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#%%
def calculo_clasificadores():
    '''Repite 100 veces la partición, entrenamiento y evalución. 
    Entrená el clasificador sobre el conjunto train y evaluáloa 
    sobre el conjunto test'''
    
    iris_dataset = load_iris()
    res_knn = []
    res_clf = []
    res_rfc = []

    for n in range(100):
        #Partición del conjunto original en test y train aleatoriamente
        X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                                            iris_dataset['target'])
        
        knn = KNeighborsClassifier(n_neighbors = 1)
        knn.fit(X_train, y_train)                       #Entrenamiento de knn
        res_knn.append(knn.score(X_test, y_test))       #Evaluacion del score
        
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)                       #Entrenamiento de clf
        res_clf.append(clf.score(X_test, y_test))       #Evaluacion del score

        rfc = RandomForestClassifier()
        rfc.fit(X_train, y_train)                       #Entrenamiento de rfc
        res_rfc.append(clf.score(X_test, y_test))       #Evaluacion del score

    prom_knn = sum(res_knn)/len(res_knn)
    prom_clf = sum(res_clf)/len(res_clf)
    prom_rfc = sum(res_rfc)/len(res_rfc)

    return prom_knn, prom_clf, prom_rfc 

if __name__ == '__main__':
    
    prom_knn, prom_clf, prom_rfc  = calculo_clasificadores()
    
    print(f'Promedio con KNeighbors Classifier:{prom_knn:.4f}' )
    print(f'Promedio con Decision Tree Classifier:{prom_clf:.4f}' )
    print(f'Promedio con Random Forest Classifier:{prom_rfc:.4f}' )
    
