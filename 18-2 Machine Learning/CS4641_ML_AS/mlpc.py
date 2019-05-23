import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
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

def evaluate(dt, testx, testy):
    predict_y = dt.predict(testx)
    mse = mean_squared_error(testy, predict_y, multioutput='uniform_average')
    score = accuracy_score(testy, predict_y)
    # wrong = predict_y-testy
    # wrong = np.abs(wrong)
    # total_wrong = np.sum(wrong) / float(wrong.shape[0])
    # print("the number of wrong labels : ", total_wrong)

    return score

def build_loan_mlpc(hidden_layer_sizes = (11)):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=hidden_layer_sizes)
    x, y, features = get_loan(data = "train")
    clf.fit(x,y)
    return clf

def build_gender_mlpc(hidden_layer_sizes = (20)):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=hidden_layer_sizes)
    x, y, features = get_gender(data= "train")
    clf.fit(x,y)
    return clf

layer_total = 7
loan_layers = []
gender_layers = []
loan_layer = [100]
gender_layer = [100]

for i in range(layer_total):
    loan_layers.append(tuple(loan_layer))
    gender_layers.append(tuple(gender_layer))
    loan_layer.append(100)
    gender_layer.append(100)


gender_acc = np.ones(layer_total, dtype = 'float64')
loan_acc = np.ones(layer_total, dtype = 'float64')

for i in range( layer_total):
    loandt = build_loan_mlpc(hidden_layer_sizes=loan_layers[i])
    loan_x, loan_y, features = get_loan(data="test")
    loan_acc[i] = evaluate(loandt, loan_x, loan_y)

    genderdt = build_gender_mlpc(hidden_layer_sizes=gender_layers[i])
    gender_x, gender_y, features = get_gender(data="test")
    gender_acc[i] = evaluate(genderdt, gender_x, gender_y)

print ("MLPC with large units - the ideal depth size for loan prediction is ", np.argmax(loan_acc)+1)
print ("MLPC with large units - the ideal depth size for gender recognition is ", np.argmax(gender_acc)+1)

gender_acc = pd.DataFrame(gender_acc, index=range(1, layer_total+1))
loan_acc = pd.DataFrame(loan_acc, index = range(1, layer_total+1))
plt.figure(1)
ax = loan_acc.plot(title="the number of big layers and accuracy of MLPC on loan prediction", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("MLPC_loan_biglayers.png")
plt.figure(2)
ax = gender_acc.plot(title="the number of big layers and accuracy of MLPC on voice recognition", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("MLPC_gender_biglayers.png")

layer_total = 40
loan_layers = []
gender_layers = []
loan_layer = [20]
gender_layer = [20]

for i in range(layer_total):
    loan_layers.append(tuple(loan_layer))
    gender_layers.append(tuple(gender_layer))
    loan_layer.append(20)
    gender_layer.append(20)


gender_acc = np.ones(layer_total, dtype = 'float64')
loan_acc = np.ones(layer_total, dtype = 'float64')

for i in range( layer_total):
    loandt = build_loan_mlpc(hidden_layer_sizes=loan_layers[i])
    loan_x, loan_y, features = get_loan(data="test")
    loan_acc[i] = evaluate(loandt, loan_x, loan_y)

    genderdt = build_gender_mlpc(hidden_layer_sizes=gender_layers[i])
    gender_x, gender_y, features = get_gender(data="test")
    gender_acc[i] = evaluate(genderdt, gender_x, gender_y)

print ("MLPC with large units - the ideal depth size for loan prediction is ", np.argmax(loan_acc)+1)
print ("MLPC with large units - the ideal depth size for gender recognition is ", np.argmax(gender_acc)+1)

gender_acc = pd.DataFrame(gender_acc, index=range(1, layer_total+1))
loan_acc = pd.DataFrame(loan_acc, index = range(1, layer_total+1))
plt.figure(1)
ax = loan_acc.plot(title="the number of deep layers and accuracy of MLPC on loan prediction", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("MLPC_loan_deeplayers.png")
plt.figure(2)
ax = gender_acc.plot(title="the number of deep layers and accuracy of MLPC on voice recognition", grid=True, fontsize=8)
# ax.set_xlable("maximum depth")
# ax.set_ylable("Accuracy")
plt.savefig("MLPC_gender_deeplayers.png")
