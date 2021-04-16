import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
names = "A,B,C,D,E,F,G,H,I,J,K,L,M,RESULT"
names=names.split(',')
data = pd.read_csv("heart1.csv",names=names)
model = BayesianModel([("A","B"),("B","C"),("C","RESULT")]);
model.fit(data)
infer = VariableElimination(model)
q = infer.query(variables=["RESULT"],evidence={"A":22},joint=False)
print(q["RESULT"])













































