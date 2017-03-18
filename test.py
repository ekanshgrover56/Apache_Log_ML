from machinelearning import MachineLearning
ML=MachineLearning('main3.csv')
mis_clas,acc_score,y=ML.ppn_model(40,0.1,0)
print mis_clas
print acc_score
mis_clas_LR,acc_score_LR,y=ML.lr_model(1000,0)
print mis_clas_LR
print acc_score_LR
#mis_clas_ada,acc_score_ada,y=ML.ada_sd(40,0.1,0)
#print mis_clas_ada
#print acc_score_ada