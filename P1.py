import csv
attributes = ['Sky','Airtemp','Humidity','Wind','Water','Forecast','Enjoy Sport']
print('Attributes =',attributes)
num_attributes = len(attributes)-1
dataset = list(csv.reader(open('finds.csv','r')))
print(dataset)
hypothesis=['0'] * num_attributes
print("Intial Hypothesis")
print(hypothesis)
print("The Hypothesis are")
for i in range(len(dataset)):
    target = dataset[i][-1]
    if(target == 'Yes'):
        for j in range(num_attributes):
            if(hypothesis[j]=='0'):
                hypothesis[j] = dataset[i][j]
            if(hypothesis[j]!= dataset[i][j]):
                hypothesis[j]='?'
        print(i+1,'=',hypothesis)
print("Final Hypothesis")
print(hypothesis)