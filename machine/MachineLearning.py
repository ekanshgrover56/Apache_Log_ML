from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model.stochastic_gradient import SGDClassifier

class MachineLearning:

    def __init__(self, Master_DF):
        self.Data_Frame = Master_DF

    def Encoder(self,df):
        encoder = LabelEncoder()
        print("Fitting")
        encoder.fit(df)
        return encoder.transform(df)

    def Perceptorn_PreProcessing(self, x , y):
        X = self.Encoder(self.Data_Frame[x].factorize()[0])
        Y = self.Encoder(self.Data_Frame[y].factorize()[0])
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)
        sc = StandardScaler()
        sc.fit(X_train)
        X_train_std = sc.transform(X_train)
        X_test_std = sc.transform(X_test)
        return X_train_std, Y_train, X_test_std, Y_test

    def ppn_model(self,n_iter,eta0,random_state):
        self.X_train_std_uri, self.Y_train_category, self.X_test_std_uri, self.Y_test_category = self.Perceptorn_PreProcessing('uri','category')
        ppn = Perceptron(n_iter=n_iter,eta0=eta0,random_state=random_state)
        ppn.fit(self.X_train_std_uri.reshape(len(self.X_train_std_uri),1),self.Y_train_category)
        y_pred=ppn.predict(self.X_test_std_uri.reshape(len(self.X_test_std_uri),1))
        return (self.Y_test_category != y_pred).sum(),accuracy_score(self.Y_test_category, y_pred),y_pred

    def lr_model(self,c,random_state):
        lr=LogisticRegression(C=c,random_state=random_state)
        lr.fit(self.X_train_std_uri.reshape(len(self.X_train_std_uri),1),self.Y_train_category)
        y_pred=lr.predict(self.X_test_std_uri.reshape(len(self.X_test_std_uri),1))
        return (self.Y_test_category != y_pred).sum(),accuracy_score(self.Y_test_category, y_pred),y_pred

    def ada_sd(self,n_iter,eta,random_state):
        self.ada=SGDClassifier(n_iter=n_iter,eta=eta,random_state=random_state)
        self.ada.fit(self.X_train_std_uri.reshape(len(self.X_train_std_uri),1),self.Y_train_category)
        self.y_pred=self.ada.predict(self.X_test_std_uri.reshape(len(self.X_test_std_uri),1))
        return (self.Y_test_category != self.y_pred).sum(),accuracy_score(self.Y_test_category, self.y_pred),self.y_pred
