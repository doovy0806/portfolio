from __future__ import print_function

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt



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


def visualize_tree(clf, feature_names, file_name):
    dot_data = tree.export_graphviz(clf, out_file= file_name+"dt.dot")


def build_loan_dt(max_depth=1, min_samples_leaf = 10):
    x, y, features = get_loan(data = "train")
    dt = DecisionTreeClassifier(criterion="entropy", max_depth=max_depth, min_samples_leaf=min_samples_leaf)
    dt.fit(x,y)
    visualize_tree(dt, features, "loan_prediction")
    return dt

def build_gender_dt(max_depth=5, min_samples_leaf=10):
    x,y, features=get_gender(data = "train")
    dt = DecisionTreeClassifier(criterion="entropy", max_depth=max_depth, min_samples_leaf=min_samples_leaf)
    dt.fit(x,y)
    visualize_tree(dt, features, "gender_recognition_by_voice")
    return dt

def evaluate(dt, testx, testy):
    predict_y = dt.predict(testx)
    mse = mean_squared_error(testy, predict_y, multioutput='uniform_average')
    accuracy = accuracy_score(testy, predict_y)
    # wrong = predict_y-testy
    # wrong = np.abs(wrong)
    # total_wrong = np.sum(wrong) / float(wrong.shape[0])
    # print("the number of wrong labels : ", total_wrong)

    return accuracy

depth_total = 20
leaf_total = 50

gender_acc = np.ones(depth_total, dtype = 'float64')
loan_acc = np.ones(depth_total, dtype = 'float64')

for i in range(1, depth_total+1):
    loandt = build_loan_dt(max_depth=i)
    loan_x, loan_y, features = get_loan(data="test")
    loan_acc[i-1] = evaluate(loandt, loan_x, loan_y)

    genderdt = build_gender_dt(max_depth=i)
    gender_x, gender_y, features = get_gender(data="test")
    gender_acc[i-1] = evaluate(genderdt, gender_x, gender_y)

print ("the ideal depth size for loan prediction is ", np.argmax(loan_acc)+1)
print ("the ideal depth size for gender recognition is ", np.argmax(gender_acc)+1)

gender_acc = pd.DataFrame(gender_acc, index=range(1, depth_total+1))
loan_acc = pd.DataFrame(loan_acc, index = range(1, depth_total+1))
plt.figure(1)
ax = loan_acc.plot(title="max depth and accuracy of DT on loan prediction", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("DT_loan_depth.png")
plt.figure(2)
ax = gender_acc.plot(title="max depth and accuracy of DT on gender recognition by voice", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("DT_gender_depth.png")





gender_acc = np.ones(leaf_total, dtype = 'float64')
loan_acc = np.ones(leaf_total, dtype = 'float64')

for i in range(1, leaf_total+1):
    loandt = build_loan_dt(min_samples_leaf=i)
    loan_x, loan_y, features = get_loan(data="test")
    loan_acc[i-1] = evaluate(loandt, loan_x, loan_y)

    genderdt = build_gender_dt(min_samples_leaf=i)
    gender_x, gender_y, features = get_gender(data="test")
    gender_acc[i-1] = evaluate(genderdt, gender_x, gender_y)

print ("the ideal leaf samples for loan prediction is ", np.argmax(loan_acc)+1)
print ("the ideal leaf samples for gender recognition is ", np.argmax(gender_acc)+1)
gender_acc = pd.DataFrame(gender_acc, index=range(1, leaf_total+1))
loan_acc = pd.DataFrame(loan_acc, index = range(1, leaf_total+1))
plt.figure(3)
ax = loan_acc.plot(title="leaf sample size and accuracy of DT on loan prediction", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("DT_loan_leaf.png")
plt.figure(4)
ax = gender_acc.plot(title="leaf sample size and accuracy of DT on gender recognition by voice", grid=True, fontsize=10)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("DT_gender_leaf.png")
