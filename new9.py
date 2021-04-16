from sklearn import datasets , metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
iris=datasets.load_iris()
X_train,X_test,y_train,y_test=train_test_split(iris.data,iris.target)
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
model.score
y=metrics.accuracy_score(y_test,model.predict(X_test))
print("Correct Prediction : ",y)
print("\nWrong Prediction: ",1-y)
