import numpy as np 
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)  
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X,axis=0) 
y = y/100
print("Normalized Input: \n" + str(X))
print("Actual Output: \n" + str(y))
def sigmoid(x):
    return 1/(1 + np.exp(-x))
wh=np.random.uniform(size=(2,3))
bh=np.random.uniform(size=(1,3)) 
wout=np.random.uniform(size=(3,1))
bout=np.random.uniform(size=(1,1))
for i in range(1000):
    h_act = sigmoid(np.dot(X,wh)+bh)  
    output = sigmoid(np.dot(h_act,wout)+bout)   
print("Predicted Output: \n" ,output)