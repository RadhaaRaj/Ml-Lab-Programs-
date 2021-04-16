{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Iris Data set loaded...\n",
      "Dataset is split into training and testing...\n",
      "Size of trainng data and its label (135, 4) (135,)\n",
      "Size of trainng data and its label (15, 4) (15,)\n",
      "Label 0 - setosa\n",
      "Label 1 - versicolor\n",
      "Label 2 - virginica\n",
      "Results of Classification using K-nn with K=1\n",
      " Sample: [5.4 3.9 1.3 0.4] Actual-label: 0  Predicted-label: 0\n",
      " Sample: [5.8 2.7 5.1 1.9] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [7.7 2.6 6.9 2.3] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [7.1 3.  5.9 2.1] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [6.1 3.  4.9 1.8] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [5.4 3.9 1.7 0.4] Actual-label: 0  Predicted-label: 0\n",
      " Sample: [6.7 3.3 5.7 2.5] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [6.7 3.  5.2 2.3] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [6.5 3.  5.5 1.8] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [6.1 3.  4.6 1.4] Actual-label: 1  Predicted-label: 1\n",
      " Sample: [6.3 2.9 5.6 1.8] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [4.8 3.  1.4 0.1] Actual-label: 0  Predicted-label: 0\n",
      " Sample: [5.  3.5 1.6 0.6] Actual-label: 0  Predicted-label: 0\n",
      " Sample: [6.3 2.5 5.  1.9] Actual-label: 2  Predicted-label: 2\n",
      " Sample: [6.  3.  4.8 1.8] Actual-label: 2  Predicted-label: 1\n",
      "Classification Accuracy : 0.9333333333333333\n"
     ]
    }
   ],
   "source": [
    "# import the required packages\n",
    "from sklearn.model_selection import train_test_split \n",
    "from sklearn.neighbors import KNeighborsClassifier \n",
    "from sklearn import datasets\n",
    "\n",
    "# Load dataset \n",
    "iris=datasets.load_iris() \n",
    "print(\"Iris Data set loaded...\")\n",
    "# Split the data into train and test samples\n",
    "x_train, x_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.1) \n",
    "print(\"Dataset is split into training and testing...\")\n",
    "print(\"Size of trainng data and its label\",x_train.shape,y_train.shape) \n",
    "print(\"Size of trainng data and its label\",x_test.shape, y_test.shape)\n",
    "# Prints Label no. and their names \n",
    "for i in range(len(iris.target_names)):\n",
    "    print(\"Label\", i , \"-\",str(iris.target_names[i]))\n",
    "\n",
    "# Create object of KNN classifier\n",
    "classifier = KNeighborsClassifier(n_neighbors=1)\n",
    "\n",
    "# Perform Training\n",
    "classifier.fit(x_train, y_train) \n",
    "# Perform testing\n",
    "y_pred=classifier.predict(x_test)\n",
    "\n",
    "# Display the results\n",
    "print(\"Results of Classification using K-nn with K=1\") \n",
    "for r in range(0,len(x_test)):\n",
    "    print(\" Sample:\", str(x_test[r]), \"Actual-label:\", str(y_test[r]), \" Predicted-label:\",str(y_pred[r]))\n",
    "print(\"Classification Accuracy :\" , classifier.score(x_test,y_test));"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
