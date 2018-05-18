# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import numpy as np

class DoglNet:
    def __init__(self):
        self.clf = MLPClassifier(verbose = True, solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(8,8,8), random_state=1)
        self.trained = False
        self.scaler = StandardScaler()
    def initModel(self):
        if not self.trained:
            print("Training Model")
            X = np.loadtxt(dir_path+"\DOGL_DATASET.csv",skiprows=1,delimiter=",",usecols=(1,2,3,4))
            Y = np.loadtxt(dir_path+"\DOGL_DATASET.csv",skiprows=1,delimiter=",",usecols=(5))
            X_train = X[:230,:]
            Y_train = Y[:230]
            X_test = X[230:,:]
            Y_test = Y[230:]
            self.scaler.fit(X_train)
            X_train = self.scaler.transform(X_train)
            X_test = self.scaler.transform(X_test)
            self.clf.fit(X_train,Y_train)
            predictions = self.clf.predict(X_test)
            predictions1 =self.clf.predict(X_train)
            print(confusion_matrix(Y_train,predictions1))
            print(classification_report(Y_train,predictions1))
            print(confusion_matrix(Y_test,predictions))
            print(classification_report(Y_test,predictions))
            self.trained = True
        else:
            print("Model already trained")
    
    def predict(self, predictionVector):
        if self.trained:
            data = self.scaler.transform(predictionVector)
            return self.clf.predict_proba(data)
        else:
            self.initModel()
            data = self.scaler.transform(predictionVector)
            return self.clf.predict_proba(data)
            
