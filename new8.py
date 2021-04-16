# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:06:52 2021

@author: Radha
"""

from sklearn import datasets,metrics 
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
X_train,X_test,y_train,y_test = train_test_split(iris.data,iris.target)

#KMeans Algorithm accuracy score
model = KMeans(n_clusters=3)
model.fit(X_train,y_train)
model.score
print(metrics.accuracy_score(y_test,model.predict(X_test)))

#EM Algorithm accuracy score
from sklearn.mixture import GaussianMixture
model2=GaussianMixture(n_components=3)
model2.fit(X_train,y_train)
model2.score
print(metrics.accuracy_score(y_test,model2.predict(X_test))) 