import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pli
def gtid():
	return 903456821 # replace with your GT ID number
def get_spin_result(win_prob):
	result = False
	if np.random.random() <= win_prob:
		result = True
	return result

win_prob = 18.0/40.0  # set appropriately to the probability of a win
np.random.seed(gtid())  # do this only once
print get_spin_result(win_prob)  # test the roulette spin

# add your code here to implement the experiments

#figure1

#x1 = np.array([np.arange(1001) for t in range(10)])
x1 = np.arange(1001)
y1 = np.zeros((10, 1001))

ex1winnings =0
for j in range(10):
    winnings = np.zeros(1001)
    i = 1
    bet_amount = 1
    won = False
    while winnings[i - 1] < 80 and i < 1001 :
        won = get_spin_result(win_prob)
        if won:
            winnings[i] = winnings[i - 1] + bet_amount
            bet_amount = 1
        else:
            winnings[i] = winnings[i - 1] - bet_amount
            bet_amount *= 2

        if winnings[i] >= 80:
            winnings[i:] = 80

        i += 1
    y1[j] = winnings

plt.figure(1)
plt.plot(x1, y1[0], x1, y1[1], x1, y1[2], x1, y1[3], x1, y1[4], x1, y1[5], x1, y1[6], x1, y1[7], x1, y1[8], x1, y1[9])
plt.ylim(-256, 100)
plt.xlim(0, 300)
plt.savefig("figure1.png")
#figure1  ends here

x2 = np.arange(1001)
y2 = np.zeros((1000, 1001))
for j in range(1000):
    bet_times = 1001
    winnings = np.zeros(bet_times)
    i = 1
    bet_amount = 1
    won = False
    while winnings[i - 1] < 80 and i < bet_times :
        won = get_spin_result(win_prob)
        if won:
            winnings[i] = winnings[i - 1] + bet_amount
            bet_amount = 1
        else:
            winnings[i] = winnings[i - 1] - bet_amount
            bet_amount *= 2

        if winnings[i] >= 80:
            winnings[i:] = 80
            ex1winnings +=1
            break
        i += 1

    y2[j] = winnings
print(ex1winnings/1000.0)

meanPlusSd= np.mean(y2, axis=0) + np.std(y2, axis=0)
meanMinusSd = np.mean(y2, axis=0) -  np.std(y2, axis=0)
plt.figure(2)
plt.plot(x2, np.mean(y2, axis=0), x2, meanPlusSd, x2, meanMinusSd)
plt.ylim(-256, 100)
plt.xlim(0, 300)
plt.savefig("figure2.png")

medianPlusSd= np.median(y2, axis=0) + np.std(y2, axis=0)
medianMinusSd = np.median(y2, axis=0) -  np.std(y2, axis=0)
plt.figure(3)
plt.plot(x2, np.median(y2, axis=0), x2, medianPlusSd, x2, medianMinusSd)
plt.ylim(-256, 100)
plt.xlim(0, 300)
plt.savefig("figure3.png")

# delete this part
plt.figure(6)
plt.plot(x1, np.std(y2, axis=0))
plt.savefig("figure_ex1_sd.png")
# delete


#experiment2 figure 4
x4 = np.arange(1001)
y4 = np.zeros((1000, 1001))

ex2winnings =0
ex2expvalue=0
for j in range(1000):
    bet_times = 1001
    winnings = np.zeros(bet_times)
    i = 1
    bet_amount = 1
    won = False
    while winnings[i - 1] < 80 and i < bet_times :
        won = get_spin_result(win_prob)
        if won:
            winnings[i] = winnings[i - 1] + bet_amount
            bet_amount = 1
        else:
            winnings[i] = winnings[i - 1] - bet_amount
            bet_amount *= 2
            if winnings[i] <= -256 :
                winnings[i:] = -256
                ex2expvalue += -256/1000.0
                break
            elif winnings[i] - bet_amount < -256:
                bet_amount = 256 + winnings[i]

        if winnings[i] >= 80:
            winnings[i:] = 80
            ex2winnings+=1
            ex2expvalue += 80/1000.0
            break
        if i==bet_times-1 :
            ex2expvalue += winnings[i]/1000.0
        i += 1

    y4[j] = winnings

print(ex2winnings/1000.0)
print("expected: ", ex2expvalue)

plt.figure(4)
meanPlusSd_2 = np.mean(y4, axis=0) + np.std(y4, axis=0)
meanMinusSd_2 = np.mean(y4, axis=0) - np.std(y4, axis=0)
plt.plot(x4, np.mean(y4, axis=0), x4, meanPlusSd_2, x4, meanMinusSd_2)
plt.xlim(0,300)
plt.ylim(-256,100)
plt.savefig("figure4.png")

plt.figure(5)
medianPlusSd_2 = np.median(y4, axis=0) + np.std(y4, axis=0)
medianMinusSd_2 = np.median(y4, axis=0) - np.std(y4, axis=0)
plt.plot(x4, np.median(y4, axis=0), x4, medianPlusSd_2, x4, medianMinusSd_2)
plt.xlim(0,300)
plt.ylim(-256,100)
#f1 = pli.FigureImage(1)
plt.savefig("figure5.png")

# delete this part
plt.figure(7)
plt.plot(x1, np.std(y4, axis=0))
std = np.std(y4,axis=0)
print(std[1000])
plt.savefig("figure_ex2_sd.png")
# delete