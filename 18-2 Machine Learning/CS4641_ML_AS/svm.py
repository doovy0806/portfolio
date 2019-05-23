import pandas as pd
import numpy as np
from sklearn.svm import SVC, LinearSVC
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error, accuracy_score




def get_loan(data = "train"):
    """Get the iris data, from local csv or pandas repo."""
    if data=="train":
        df = pd.read_csv("loan_prediction_train.csv", index_col=0)
    elif data == "test":
        df = pd.read_csv("loan_prediction_test.csv", index_col=0)
    else :
        print("loan_data : whole")
        df = pd.read_csv("loan_prediction.csv", index_col=0)
    df= df.dropna()
    y = df["Loan_Status"]
    features = list(df.columns[:-1])
    x = df[features]

    return x, y, features


def get_gender(data = "train"):
    """Get the iris data, from local csv or pandas repo."""

    if data=="train":
        df = pd.read_csv("gender_recognition_by_voice_train.csv", index_col=False)
    elif data == "test":
        df = pd.read_csv("gender_recognition_by_voice_test.csv", index_col=False)
    else :
        print("gender_data : whole")
        df = pd.read_csv("gender_recognition_by_voice.csv", index_col=False)

    df= df.dropna()
    y= df["label"]
    features = list(df.columns[:-1])
    x=df[features]

    return x,y,features

def evaluate(dt, testx, testy):
    predict_y = dt.predict(testx)
    mse = mean_squared_error(testy, predict_y, multioutput='uniform_average')
    score = accuracy_score(testy, predict_y)
    # wrong = predict_y-testy
    # wrong = np.abs(wrong)
    # total_wrong = np.sum(wrong) / float(wrong.shape[0])
    # print("the number of wrong labels : ", total_wrong)

    return score

def build_loan_svc(kernel = 'sigmoid'):
    clf = SVC(kernel=kernel)
    x, y, features = get_loan(data="train")
    clf.fit(x,y)
    return clf

def build_gender_svc(kernel = 'sigmoid'):
    clf = SVC(kernel=kernel)
    x, y, features = get_gender(data= "train")
    clf.fit(x,y)
    return clf


def build_loan_linsvc():
    clf = LinearSVC()
    x, y, features = get_loan(data= "train")
    clf.fit(x,y)
    return clf
def build_gender_linsvc():
    clf = LinearSVC()
    x, y, features = get_gender(data= "train")
    clf.fit(x,y)
    return clf
# kernels = [ 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' ]
# kernels = [ 'poly', 'rbf', 'sigmoid']
# gender_acc = np.ones(len(kernels), dtype = 'float64')
# loan_acc = np.ones(len(kernels), dtype = 'float64')
#
# for i in kernels:
#     loandt = build_loan_svc(kernel=i)
#     loan_x, loan_y, features = get_loan(data="test")
#     loan_acc[i] = evaluate(loandt, loan_x, loan_y)
#     print( "Kernel",kernels[i]," accruacy - loan : ", loan_acc[i])
#
#     genderdt = build_gender_svc(kernel=i)
#     gender_x, gender_y, features = get_gender(data="test")
#     gender_acc[i] = evaluate(genderdt, gender_x, gender_y)
#     print("Kernel", kernels[i], " accruacy - gender : ", gender_acc[i])
#
# print ("SVC - the ideal kernel for loan prediction is ", kernels[np.argmax(loan_acc)])
# print ("SVC - the ideal kernel for gender recognition is ", kernels[np.argmax(gender_acc)])
#
# gender_acc = pd.DataFrame(gender_acc, index=kernels)
# loan_acc = pd.DataFrame(loan_acc, index = kernels)
# plt.figure(1)
# ax = loan_acc.plot(title="kernels and accuracy of Boosting DT on loan prediction", grid=True, fontsize=8)
# # ax.set_xlable("maximum depth")
# # ax.set_ylable("Accuracy")
# plt.savefig("SVC_loan_kernels.png")
# plt.figure(2)
# ax = gender_acc.plot(title="kernels and accuracy of Boosting DT on gender recognition by voice", grid=True, fontsize=8)
# # ax.set_xlable("maximum depth")
# # ax.set_ylable("Accuracy")
# plt.savefig("SVC_gender_kernels.png")


loandt = build_loan_svc(kernel = "sigmoid")
loan_x, loan_y, features = get_loan(data = "test")
loan_accuracy = evaluate(loandt, loan_x, loan_y )
print ("loan SVM accuracy score : ", loan_accuracy)
genderdt = build_gender_svc(kernel="sigmoid")
gender_x, gender_y, features = get_gender(data = "test")
gender_accuracy = evaluate(genderdt, gender_x, gender_y )
print ("gender SVM accuracy score : " , gender_accuracy)

loandt = build_loan_linsvc()
loan_x, loan_y, features = get_loan(data = "test")
loan_accuracy = evaluate(loandt, loan_x, loan_y )
print ("loan linear SVM accuracy score : ", loan_accuracy)
genderdt = build_gender_linsvc()
gender_x, gender_y, features = get_gender(data = "test")
gender_accuracy = evaluate(genderdt, gender_x, gender_y )
print ("gender linear SVM accuracy score : " , gender_accuracy)
