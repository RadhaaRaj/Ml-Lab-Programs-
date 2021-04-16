import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
data=pd.read_csv('five..csv')
print("The first 5 values of data is:\n" ,data.head())
X=data.iloc[:,:-1]
print("The first 5 values of train data is:\n",X.head())
Y=data.iloc[:,-1]
print("The first 5 values of output data is:\n",Y.head( ))
le_Outlook=LabelEncoder()
X.Outlook=le_Outlook.fit_transform(X.Outlook)
le_Temperature=LabelEncoder()
X.Temperature=le_Temperature.fit_transform(X.Temperature)
le_Humidity=LabelEncoder()
X.Humidity=le_Humidity.fit_transform(X.Humidity)
le_Windy=LabelEncoder()
X.Windy=le_Windy.fit_transform(X.Windy)
print("\n Now the train data is:\n",X.head())
le_PlayTennis=LabelEncoder()
Y=le_PlayTennis.fit_transform(Y)
print("/n Now the output data is:\n",Y)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20)
Classifier=GaussianNB()
Classifier.fit(X_train,Y_train)
from sklearn.metrics import accuracy_score
print("accuracy is:",accuracy_score(Classifier.predict(X_test),Y_test))