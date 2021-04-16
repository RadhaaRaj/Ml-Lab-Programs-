from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import datasets
iris=datasets.load_iris()
iris_data=iris.data
iris_label=iris.target
print(iris_data)
print(iris_label)
x_train,x_test,y_train,y_test=train_test_split(iris_data,iris_label,test_size=0.30)
classifier=KNeighborsClassifier(n_neighbors=8,p=3,metric='euclidean')
classifier.fit(x_train,y_train)
#predict the test resuts
y_pred=classifier.predict(x_test)
cm=confusion_matrix(y_test,y_pred)
print('Confusion matrix is as follows\n',cm)
print('Accuracy Metrics')
print(classification_report(y_test,y_pred))
print(" correct predicition",accuracy_score(y_test,y_pred))
print(" wrong predicition",(1-accuracy_score(y_test,y_pred)))