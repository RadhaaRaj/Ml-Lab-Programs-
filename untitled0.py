from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
docs=fetch_20newsgroups_vectorized()
x_train,x_test,y_train,y_test=train_test_split(docs.data,docs.target)
model=MultinomialNB()
model.fit(x_train,y_train)
print("Accuracy: ",metrics.accuracy_score(y_test,model.predict(x_test)))
print("Precision:",metrics.precision_score(y_test,model.predict(x_test),average=None))
print("Recall:",metrics.recall_score(y_test,model.predict(x_test),average=None))