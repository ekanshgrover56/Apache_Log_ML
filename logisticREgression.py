from sklearn import datasets
from sklearn.cross_validation import train_test_split
import numpy as np
import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
iris=pandas.read_csv('main3.csv')
x=iris['uri']
y=iris['category']
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=0)
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
lr=LogisticRegression(C=1000.0,random_state=0)
lr.fit(X_train_std.reshape(len(X_train_std),1),Y_train)
y_pred=lr.predict(X_test_std.reshape(len(X_test_std),1))
print('Misclassified samples: %d' % (Y_test != y_pred).sum())
print('Accuracy: %.2f' % accuracy_score(Y_test, y_pred))

