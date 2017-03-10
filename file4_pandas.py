from sklearn import datasets
from sklearn.cross_validation import train_test_split
import numpy as np
import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
iris=pandas.read_csv('main3.csv') # needs preprocessed training data sets in csv file
x=iris['uri']
y=iris['category']
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=0) #splitting training and testing data as 70-30 by test_size=0.3
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
ppn=Perceptron(n_iter=40,eta0=0.1,random_state=0)
ppn.fit(X_train_std.reshape(len(X_train_std),1),Y_train)
y_pred=ppn.predict(X_test_std.reshape(len(X_test_std),1))
print('Misclassified samples: %d' % (Y_test != y_pred).sum())
print('Accuracy: %.2f' % accuracy_score(Y_test, y_pred))
