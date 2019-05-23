import numpy as np
import cv2
import os
import sys
import math

def readimg(i):
    string = "faces_training/face"+i+".pgm"
    img = cv2.imread(string, cv2.IMREAD_GRAYSCALE)
    return img
def readtestimg(i):
    string = "faces_test/test"+i+".pgm"
    img = cv2.imread(string, cv2.IMREAD_GRAYSCALE)
    return img

def project_img(img):
    imgrow = img.flatten() - np.average(img)
    newy = np.dot(w, imgrow.T)
    newyshape = newy.shape
    newx = np.dot(w.T, newy)
    newx = np.reshape(newx, (96,84))
    return newx

def recognize(img):
    min_msl = -1
    min_num = -1
    for i in range(39):
        msl = calculate_l2(img, pcaimgs[i])
        if min_msl<0:
            min_msl=msl
            min_num=i
        elif min_msl > msl :
            min_msl = msl
            min_num = i
    if min_num+1<10 :
        min_numstr = "0"+str(min_num+1)
    else:
        min_numstr=str(min_num+1)
    return min_numstr

def calculate_l2(img1, img2):
    l2sum = np.sum(np.power(img1 - img2, 2))
    l2loss = float(np.sqrt(l2sum))
    return l2loss


threshold = float(sys.argv[1])

numbers = range(1,40)

imgs = []
greyimgs =[]
imgavgs=[]
svd=[]
step1str = "##########\tSTEP1\t##########"
imgmtrx = None
pcaimgs=[]

for i in numbers:
    numstr =""
    if i<10:
        numstr = "0"+str(i)
    else:
        numstr = str(i)
    img = readimg(numstr)
    sha = np.shape(img)
    img = img.flatten()
    imgs.append(img)
    imgavgs.append(np.average(img))
    img = img-np.average(img)
    greyimgs.append(img)

imgavgs = np.array(imgavgs)
imgmtrx = np.stack(tuple(greyimgs))
imgmtrx = imgmtrx.T
# img_row_avg = np.average(imgmtrx, axis=0)
# zeromean_imgmtrx = imgmtrx[:]-np.average(imgmtrx, axis=0)
u,v,vh = np.linalg.svd(imgmtrx)
evsum=0
evlist = []
vsqaured = np.square(v)
evwhole = np.sum(vsqaured)
for ev in vsqaured:
    evsum+=ev
    evratio = np.float(evsum/evwhole)
    evlist.append(ev)
    if evratio>=threshold:
        break
step1str+="\nInput percentage: "+str(threshold)
step1str += "\nSelected Dimension: "+str(len(evlist))
evnum = len(evlist)
w = u[:,:len(evlist)]
w=w.T

STUDENT_CODE = "2014121136"
FILENAME = "output2.txt"
if not os.path.exists(STUDENT_CODE):
    os.mkdir(STUDENT_CODE)
f = open(os.path.join(STUDENT_CODE, FILENAME),'w')
f.write(step1str+"\n")
f.close()

y = np.dot(w, imgmtrx)
step2str ="\n##########\tSTEP2\t##########"
yshpae = y.shape
wty = np.dot(w.T, y)
wtyshape = wty.shape
#each column is an image
# x = wty[:] + img_row_avg
xt =wty.T
xtshape = xt.shape

mslstring =""
mslsum=0
newimgs = []

for i in range(39):
    pcaimgs.append(np.reshape(xt[i],(96,84)))
    newimg = xt[i] + imgavgs[i]
    # newimg = newimg_mtrx[i]
    newimg = np.reshape(newimg, (96,84))
    newshape = newimg.shape
    newimg = newimg.astype(int)
    newimgs.append(newimg)
    if i+1<10:
        nums = "0"+str(i+1)
    else:
        nums = str(i+1)
    cv2.imwrite(str(STUDENT_CODE)+"/face"+nums+".pgm",newimg)
    originalimg = cv2.imread("faces_training/face"+nums+".pgm", cv2.IMREAD_GRAYSCALE)
    # originalimg = originalimg[:,:,0]
    msl = np.average(np.square(originalimg-newimg))
    mslsum += msl
    mslstring += "\n"+str(nums)+": " + format(msl, ".4f")
mslavg = mslsum/39
step2str += "\nReconstruction error\naverage : "+format(mslavg, ".4f") + mslstring +"\n"
f = open(os.path.join(STUDENT_CODE, FILENAME),'a')
f.write(step2str)
f.close()

step3str = "\n##########\tSTEP3\t##########"
for i in range(5):
    numstr = "0"+str(i+1)
    testimg = readtestimg(numstr)
    # result = recognize(testimg[:,:,0])
    projected_testimg = project_img(testimg)
    result = recognize(projected_testimg)
    step3str+="\ntest"+numstr+".pgm ==> face"+result+".pgm"
f = open(os.path.join(STUDENT_CODE, FILENAME),'a')
f.write(step3str)
f.close()












