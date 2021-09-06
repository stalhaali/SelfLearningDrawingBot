import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import joblib


#Load data for fruits
data1 = np.load("trainingmodel/data/apple.npy")
data2 = np.load("trainingmodel/data/pineapple.npy")
data3 = np.load("trainingmodel/data/grapes.npy")
data4 = np.load("trainingmodel/data/banana.npy")

#Load data for vehicles
data5 = np.load("trainingmodel/data/airplane.npy")
data6 = np.load("trainingmodel/data/sailboat.npy")
data7 = np.load("trainingmodel/data/bicycle.npy")
data8 = np.load("trainingmodel/data/car.npy")

#Load data for shapes
data9 = np.load("trainingmodel/data/square.npy")
data10 = np.load("trainingmodel/data/circle.npy")
data11 = np.load("trainingmodel/data/triangle.npy")
data12 = np.load("trainingmodel/data/star.npy")

#Create training data (datax) and testing data (datax) for fruits
datax = np.concatenate((data1[:5000, :], data2[:5000, :], data3[:5000, :], data4[:5000, :]))
testx = np.concatenate((data1[5000:10000, :], data2[5000:10000, :], data3[5000:10000, :], data4[5000:10000, :]))

#Create training data (datax) and testing data (datax) for vehicles
datax2 = np.concatenate((data5[:5000, :], data6[:5000, :], data7[:5000, :], data8[:5000, :]))
testx2 = np.concatenate((data5[5000:10000, :], data6[5000:10000, :], data7[5000:10000, :], data8[5000:10000, :]))

#Create training data (datax) and testing data (datax) for shapes
datax3 = np.concatenate((data9[:5000, :], data10[:5000, :], data11[:5000, :], data12[:5000, :]))
testx3 = np.concatenate((data9[5000:10000, :], data10[5000:10000, :], data11[5000:10000, :], data12[5000:10000, :]))

#Create y data (training and testing)
lst1 = []
lst2 = []
lst3 = []
for i in range(0, 20000):
  if i < 5000:
    lst1.append('apples')
    lst2.append('airplanes')
    lst3.append('squares')
  elif 5000 <= i < 10000:
    lst1.append('pineapples')
    lst2.append('sailboats')
    lst3.append('circles')
  elif 10000 <= i < 15000:
    lst1.append('grapes')
    lst2.append('bicycles')
    lst3.append('triangles')
  else:
    lst1.append('bananas')
    lst2.append('cars')
    lst3.append('hexagons')
datay = np.array(lst1)
datay2 = np.array(lst2)
datay3 = np.array(lst3)

datab = datay.copy()
datac = datay2.copy()
datad = datay3.copy()

#Shuffle the data to make machine learning model more accurate.
rng_state = np.random.get_state()
np.random.shuffle(datax)
np.random.set_state(rng_state)
np.random.shuffle(datay)
np.random.set_state(rng_state)
np.random.shuffle(datax2)
np.random.set_state(rng_state)
np.random.shuffle(datay2)
np.random.set_state(rng_state)
np.random.shuffle(datax3)
np.random.set_state(rng_state)
np.random.shuffle(datay3)

xtrain = datax
xtrain2 = datax2
xtrain3 = datax3
train_label = datay
train_label2 = datay2
train_label3 = datay3
xtest = testx
xtest2 = testx2 
xtest3 = testx3
ytest = datab
ytest2 = datac
ytest3 = datad

#create and train model
model1 = KNeighborsClassifier(n_neighbors=5)
model2 = KNeighborsClassifier(n_neighbors=5)
model3 = KNeighborsClassifier(n_neighbors=5)
model1.fit(xtrain, train_label)
model2.fit(xtrain2, train_label2)
model3.fit(xtrain3, train_label3)

#Test model accuracy
y_predict1 = model1.predict(xtest)
y_predict2 = model2.predict(xtest2)
y_predict3 = model3.predict(xtest3)

#prints model's accuracy
count = 0
count2 = 0
count3 = 0
for i in range(0, 20000):
  count += 1 if y_predict1[i] == ytest[i] else 0
  count2 += 1 if y_predict2[i] == ytest2[i] else 0
  count3 += 1 if y_predict3[i] == ytest3[i] else 0

print((count/20000) * 100)
print((count2/20000) * 100)
print((count3/20000) * 100)

#save model
joblib.dump(model1, 'model_joblib')
joblib.dump(model2, 'mode2_joblib')
joblib.dump(model3, 'mode3_joblib')
