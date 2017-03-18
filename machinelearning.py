from sklearn import datasets
from sklearn.cross_validation import train_test_split
import numpy as np
import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import stochastic_gradient

class MachineLearning:
    def __init__(self,fname):
        self.data=pandas.read_csv(fname)
        self.x=self.data['uri']
        self.y=self.data['category']
        self.X_train,self.X_test,self.Y_train,self.Y_test=train_test_split(self.x,self.y,test_size=0.3,random_state=0)
        self.sc=StandardScaler()
        self.sc.fit(self.X_train)
        self.X_train_std=self.sc.transform(self.X_train)
        self.X_test_std=self.sc.transform(self.X_test)
    def ppn_model(self,n_iter,eta0,random_state):
        self.ppn=Perceptron(n_iter=n_iter,eta0=eta0,random_state=random_state)
        self.ppn.fit(self.X_train_std.reshape(len(self.X_train_std),1),self.Y_train)
        self.y_pred=self.ppn.predict(self.X_test_std.reshape(len(self.X_test_std),1))
        return (self.Y_test != self.y_pred).sum(),accuracy_score(self.Y_test, self.y_pred),self.y_pred
    def lr_model(self,c,random_state):
        self.lr=LogisticRegression(C=c,random_state=random_state)
        self.lr.fit(self.X_train_std.reshape(len(self.X_train_std),1),self.Y_train)
        self.y_pred=self.lr.predict(self.X_test_std.reshape(len(self.X_test_std),1))
        return (self.Y_test != self.y_pred).sum(),accuracy_score(self.Y_test, self.y_pred),self.y_pred
    '''def ada_sd(self,n_iter,eta,random_state):
        self.ada=stochastic_gradient(n_iter=n_iter,eta=eta,random_state=random_state)
        self.ada.fit(self.X_train_std.reshape(len(self.X_train_std),1),self.Y_train)
        self.y_pred=self.ada.predict(self.X_test_std.reshape(len(self.X_test_std),1))
        return (self.Y_test != self.y_pred).sum(),accuracy_score(self.Y_test, self.y_pred),self.y_pred'''
        