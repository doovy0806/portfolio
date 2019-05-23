import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as knn
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

def build_loan_knn(n_neighbors = 200):
    clf = knn(n_neighbors=n_neighbors)
    x, y, features = get_loan(data="train")
    clf.fit(x,y)
    return clf

def build_gender_knn(n_neighbors = 100):
    clf = knn(n_neighbors= n_neighbors)
    x, y, features = get_gender(data= "train")
    clf.fit(x,y)
    return clf

n_total_loan = 300
n_total_gender = 2000
# leaf_total = 50



gender_acc = np.ones(n_total_gender, dtype = 'float64')
loan_acc = np.ones(n_total_loan, dtype = 'float64')

for i in range(n_total_loan):
    loandt = build_loan_knn(n_neighbors=i+1)
    loan_x, loan_y, features = get_loan(data="test")
    loan_acc[i] = evaluate(loandt, loan_x, loan_y)

for i in range(n_total_gender):
    genderdt = build_gender_knn(n_neighbors=i+1)
    gender_x, gender_y, features = get_gender(data="test")
    gender_acc[i] = evaluate(genderdt, gender_x, gender_y)

print ("KNN - the ideal k size for loan prediction is ", np.argmax(loan_acc)+1)
print ("Boosting - the ideal k size for gender recognition is ", np.argmax(gender_acc)+1)

gender_acc = pd.DataFrame(gender_acc, index=range(1, n_total_gender+1))
loan_acc = pd.DataFrame(loan_acc, index = range(1, n_total_loan+1))
plt.figure(1)
ax = loan_acc.plot(title="max depth and accuracy of Boosting DT on loan prediction", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("KNN_loan_K.png")
plt.figure(2)
ax = gender_acc.plot(title="max depth and accuracy of Boosting DT on gender recognition by voice", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("KNN_gender_K.png")

#
# loandt = build_loan_knn()
# loan_x, loan_y, features = get_loan(data = "test")
# loan_accuracy = evaluate(loandt, loan_x, loan_y )
# print ("loan KNN accuracy score : ", loan_accuracy)
# genderdt = build_gender_knn()
# gender_x, gender_y, features = get_gender(data = "test")
# gender_accuracy = evaluate(genderdt, gender_x, gender_y )
# print ("gender KNN accuracy score : " , gender_accuracy)
#
