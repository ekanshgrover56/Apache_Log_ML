from mongo.MongoGrabber import Mongo_Grabber
from machine.MachineLearning import MachineLearning


dbconnector = Mongo_Grabber('capstone2','123456','169.45.94.131','32156')
Master_DF = dbconnector.get_data('http_bank')

print("DataFrame Created\nStarting Prceptron Model")

ML = MachineLearning(Master_DF)
mis_clas,acc_score,y = ML.ppn_model(40,0.1,0)

print("Perceptron Accuracy Score {}".format(acc_score))

mis_clas_lr,acc_score_lr,y_lr = ML.lr_model(1000,0)

print("LogisticRegression Accuracy Score {}".format(acc_score_lr))


#mis_clas_ada,acc_score_ada,y_ada = ML.ada_sd(20,0.1, 0)
